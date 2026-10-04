import Foundation
import Observation

@MainActor @Observable
final class MathBuddyStore {
    private(set) var route: AppRoute = .home
    private(set) var session: SessionCheckpoint?
    private(set) var settings = ParentSettings()
    private(set) var inventory = GardenInventory()
    private(set) var stats: [ActivityKind: ActivityStats] = [:]
    private(set) var storageNotice: String?

    @ObservationIgnored private let storageURL: URL
    @ObservationIgnored private var unreadableSave = false

    init(storageURL: URL? = nil) {
        self.storageURL = storageURL ?? FileManager.default.urls(
            for: .applicationSupportDirectory, in: .userDomainMask
        )[0].appendingPathComponent("MathBuddy", isDirectory: true)
            .appendingPathComponent("progress-v1.json")
        load()
    }

    var round: RoundState? {
        guard let session, session.rounds.indices.contains(session.currentIndex) else { return nil }
        return session.rounds[session.currentIndex]
    }
    var roundNumber: Int { (session?.currentIndex ?? 0) + 1 }
    var sessionRoundCount: Int { session?.rounds.count ?? settings.sessionLength }
    var hasUnfinishedSession: Bool { session != nil && session?.isComplete == false }
    var canUndo: Bool {
        guard let round, route == .activity else { return false }
        return (round.phase == .interacting && !round.moveHistory.isEmpty)
            || (round.kind == .addition && round.phase == .answering)
    }

    func startOrResume() {
        if hasUnfinishedSession {
            route = .activity
            save()
        } else {
            newSession()
        }
    }

    // UI requests adult confirmation before replacing an unfinished session.
    func newSession() {
        session = .authored(settings: settings)
        route = .activity
        save()
    }

    func goHome() { route = .home; save() }
    func openGarden() { route = .garden; save() }
    func finishForNow() { route = .goodbye; save() }

    func toggleObject(_ objectID: Int) {
        mutateRound { round in
            guard round.phase == .interacting, round.kind != .addition,
                  (0..<round.total).contains(objectID) else { return }
            round.moveHistory.append(round.selected)
            if round.selected.contains(objectID) { round.selected.remove(objectID) }
            else { round.selected.insert(objectID) }
            round.feedback = nil
        }
    }

    func undo() {
        mutateRound { round in
            if round.kind == .addition, round.phase == .answering {
                round.phase = .interacting
                round.feedback = nil
            } else if round.phase == .interacting, let previous = round.moveHistory.popLast() {
                round.selected = previous
                round.feedback = nil
            }
        }
    }

    func checkCount() {
        guard let round, round.kind == .counting, round.phase == .interacting else { return }
        submit(correct: round.selected.count == round.countTarget,
               retry: round.selected.count > round.countTarget
                ? "Let's give some berries back. We need \(round.countTarget)."
                : "Let's count the berries in the basket. We need \(round.countTarget).")
    }

    func joinGroups() {
        mutateRound { round in
            guard round.kind == .addition, round.phase == .interacting else { return }
            round.phase = .answering
            round.feedback = nil
        }
    }

    func checkTransfer() {
        guard let current = round, current.kind == .subtraction, current.phase == .interacting else { return }
        if current.selected.count == current.takeAway {
            mutateRound { round in
                recordSubmission(correct: true, round: &round)
                round.phase = .answering
                round.feedback = nil
            }
        } else {
            mutateRound { round in
                recordSubmission(correct: false, round: &round)
                round.feedback = "Our friend needs \(round.takeAway) berries. You can move them back, too."
                if round.incorrectSubmissions >= 2 { provideHelp(round: &round) }
            }
        }
    }

    func chooseAnswer(_ value: Int) {
        guard let round, round.phase == .answering, round.answerOptions.contains(value) else { return }
        submit(correct: value == round.answer, retry: "Let's count the berries together. Try another number.")
    }

    func requestHelp() {
        mutateRound { round in
            guard round.phase != .success else { return }
            provideHelp(round: &round)
        }
    }

    func advance() {
        guard route == .activity, var checkpoint = session,
              checkpoint.rounds[checkpoint.currentIndex].phase == .success,
              !checkpoint.isComplete else { return }
        if checkpoint.currentIndex + 1 < checkpoint.rounds.count {
            checkpoint.currentIndex += 1
        } else {
            checkpoint.completedAt = Date()
            // The checkpoint and grant share one atomic file. Repeated Continue cannot grant twice.
            inventory.completedSessionIDs.insert(checkpoint.id)
            route = .garden
        }
        session = checkpoint
        save()
    }

    func placePinwheel() {
        guard inventory.ownsPinwheel else { return }
        inventory.pinwheelPlaced = true
        save()
    }

    func updateSettings(_ proposed: ParentSettings) {
        var valid = proposed
        valid.sessionLength = proposed.sessionLength == 5 ? 5 : 3
        settings = valid
        save()
    }

    // The parent UI must confirm this destructive action.
    func resetProgress() {
        session = nil
        inventory = GardenInventory()
        stats = [:]
        route = .home
        unreadableSave = false
        save()
    }

    func save() {
        guard !unreadableSave else {
            storageNotice = "The saved garden could not be read. It has been kept safe. A grown-up can reset local progress to save a new garden."
            return
        }
        do {
            let snapshot = SavedProgress(route: route, settings: settings, inventory: inventory,
                                         stats: stats, session: session)
            guard snapshot.isValid else { throw StorageError.invalidProgress }
            let encoder = JSONEncoder()
            encoder.outputFormatting = [.sortedKeys]
            let data = try encoder.encode(snapshot)
            try FileManager.default.createDirectory(at: storageURL.deletingLastPathComponent(),
                                                    withIntermediateDirectories: true)
            try data.write(to: storageURL, options: .atomic)
            storageNotice = nil
        } catch {
            storageNotice = "Progress is still here, but could not be saved. \(error.localizedDescription)"
        }
    }

    private func load() {
        guard FileManager.default.fileExists(atPath: storageURL.path) else { return }
        do {
            let data = try Data(contentsOf: storageURL)
            let saved = try JSONDecoder().decode(SavedProgress.self, from: data)
            guard saved.isValid else { throw StorageError.invalidProgress }
            route = saved.route
            settings = saved.settings
            session = saved.session
            inventory = saved.inventory
            stats = saved.stats
        } catch {
            unreadableSave = true
            storageNotice = "The saved garden could not be read. It has been kept safe. A grown-up can reset local progress to save a new garden."
        }
    }

    private func mutateRound(_ operation: (inout RoundState) -> Void) {
        guard route == .activity, var checkpoint = session, !checkpoint.isComplete else { return }
        operation(&checkpoint.rounds[checkpoint.currentIndex])
        session = checkpoint
        save()
    }

    private func submit(correct: Bool, retry: String) {
        guard route == .activity, let current = round, current.phase != .success else { return }
        mutateRound { round in
            recordSubmission(correct: correct, round: &round)
            if correct {
                round.phase = .success
                round.completedAt = Date()
                round.feedback = "You helped Pip!"
                var evidence = stats[round.kind, default: ActivityStats()]
                evidence.completed += 1
                if round.helpUsed { evidence.withHelp += 1 }
                stats[round.kind] = evidence
            } else {
                round.feedback = retry
                if round.incorrectSubmissions >= 2 { provideHelp(round: &round) }
            }
        }
    }

    private func recordSubmission(correct: Bool, round: inout RoundState) {
        round.submittedAnswers += 1
        if !correct { round.incorrectSubmissions += 1 }
        if round.firstSubmissionCorrect == nil { round.firstSubmissionCorrect = correct }
    }

    private func provideHelp(round: inout RoundState) {
        round.helpUsed = true
        switch round.kind {
        case .counting:
            round.moveHistory.append(round.selected)
            round.selected = Set(0..<round.countTarget)
            round.feedback = "Let's pack together: \(round.countTarget) berries. Count them, then tap Done."
        case .addition:
            round.phase = .answering
            round.feedback = "\(round.addLeft) and \(round.addRight) make \(round.answer). Count them, then choose \(round.answer)."
        case .subtraction:
            if round.phase == .interacting {
                round.moveHistory.append(round.selected)
                round.selected = Set(0..<round.takeAway)
                round.feedback = "Let's give our friend \(round.takeAway) berries. Count their plate, then tap Done."
            } else {
                round.feedback = "\(round.answer) berries are left on Pip's mat. Count them, then choose \(round.answer)."
            }
        }
    }

    private enum StorageError: LocalizedError {
        case invalidProgress
        var errorDescription: String? { "The saved progress format could not be validated." }
    }
}
