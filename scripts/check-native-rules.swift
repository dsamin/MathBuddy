import Foundation

// Compile alongside MathBuddy/Model/*.swift. Every check uses a throwaway save directory.
@main
struct NativeRuleChecks {
    @MainActor
    static func main() throws {
        let directory = FileManager.default.temporaryDirectory
            .appendingPathComponent("MathBuddy-rule-checks-\(UUID().uuidString)")
        try FileManager.default.createDirectory(at: directory, withIntermediateDirectories: true)
        defer { try? FileManager.default.removeItem(at: directory) }
        let save = directory.appendingPathComponent("progress.json")
        var store = MathBuddyStore(storageURL: save)

        expect(store.stats.isEmpty && !store.inventory.ownsPinwheel, "Fresh profiles contain no sample progress")
        store.startOrResume()
        expect(store.sessionRoundCount == 3 && store.round?.kind == .counting, "Default authored mixed session")
        expect(store.round?.total == 6 && store.round?.countTarget == 5, "Count a subset of the larger tray")
        store.toggleObject(-1)
        store.toggleObject(99)
        expect(store.round?.selected.isEmpty == true, "Invalid piece IDs are ignored")
        store.toggleObject(0)
        store.checkCount()
        expect(store.round?.phase == .interacting && store.round?.selected == [0], "A miss preserves the scene")
        store.toggleObject(1)
        store.undo()
        expect(store.round?.selected == [0], "Undo returns exactly the previous selection")
        let stableRoundID = store.round?.id
        store.goHome()
        store = MathBuddyStore(storageURL: save)
        store.startOrResume()
        expect(store.round?.id == stableRoundID && store.round?.selected == [0], "Relaunch resumes piece identities and locations")
        store.requestHelp()
        expect(store.round?.helpUsed == true && store.round?.selected.count == 5, "Help visibly models a valid set")
        store.undo()
        expect(store.round?.helpUsed == true && store.round?.selected == [0], "Undo never erases assistance evidence")
        store.requestHelp()
        store.checkCount()
        store.checkCount()
        expect(store.stats[.counting]?.completed == 1 && store.stats[.counting]?.withHelp == 1, "Round completion is idempotent and help is recorded")
        store = MathBuddyStore(storageURL: save)
        store.checkCount()
        expect(store.stats[.counting]?.completed == 1, "Relaunch does not recount a completed round")
        store.advance()

        store.chooseAnswer(3)
        expect(store.round?.phase == .interacting, "Addition requires visible joining first")
        store.joinGroups()
        store.undo()
        expect(store.round?.phase == .interacting, "Joined groups can be separated before answering")
        store.joinGroups()
        store.chooseAnswer(2)
        expect(store.round?.isJoined == true && store.round?.phase == .answering, "Wrong numeral preserves joined objects")
        store.chooseAnswer(3)
        expect(store.stats[.addition]?.withoutHelp == 1, "Retry without extra help remains distinct from modeled help")
        store.advance()

        store.toggleObject(4)
        store.checkTransfer()
        expect(store.round?.phase == .interacting && store.round?.selected == [4], "Subtraction under-transfer is recoverable")
        store.chooseAnswer(3)
        expect(store.round?.phase == .interacting, "Remaining-total answer cannot skip transfer checkpoint")
        store.toggleObject(0)
        store.checkTransfer()
        expect(store.round?.phase == .answering, "Correct transfer enters remaining-total question")
        store.toggleObject(0)
        expect(store.round?.selected == [0, 4], "Transferred pieces remain fixed during total question")
        store.chooseAnswer(3)
        expect(store.inventory.completedSessions == 0, "Reward waits for deliberate final Continue")
        store = MathBuddyStore(storageURL: save)
        store.advance()
        expect(store.inventory.completedSessions == 1 && store.route == .garden, "Completion and reward are saved together")
        store.advance()
        store.placePinwheel()
        store = MathBuddyStore(storageURL: save)
        expect(store.inventory.completedSessions == 1 && store.inventory.pinwheelPlaced, "Repeated Continue and relaunch preserve one reward")
        store.finishForNow()
        store.startOrResume()
        store.finishForNow()
        expect(store.inventory.ownsPinwheel && store.hasUnfinishedSession, "Stopping early retains owned toys and unfinished work")

        var settings = store.settings
        settings.sessionLength = 5
        store.updateSettings(settings)
        expect(store.sessionRoundCount == 3, "Settings cannot replace active content")
        store.newSession()
        for index in 0..<5 {
            finishRound(store)
            store.advance()
            expect(store.inventory.completedSessions == (index == 4 ? 2 : 1), "Five-round session grants only after its fifth round")
        }
        settings.practiceMode = .counting
        store.updateSettings(settings)
        store.newSession()
        expect(store.session?.rounds.allSatisfy { $0.kind == .counting } == true, "Counting-only entry does not introduce operations")
        expect(store.session?.rounds.allSatisfy { $0.total > $0.countTarget } == true, "Authored counting always requires making a subset")
        expect(RoundState.counting(target: 0, available: 3, contentID: "validation-zero").isValid, "Zero is a valid empty-set definition")
        expect(store.storageNotice == nil, "Successful writes clear storage notice")

        let corrupt = directory.appendingPathComponent("corrupt.json")
        let badData = Data("{broken".utf8)
        try badData.write(to: corrupt)
        let damaged = MathBuddyStore(storageURL: corrupt)
        damaged.startOrResume()
        expect(damaged.storageNotice != nil, "An unreadable save is disclosed")
        let preservedData = try Data(contentsOf: corrupt)
        expect(preservedData == badData, "An unreadable save is never overwritten by ordinary play")
        damaged.resetProgress()
        expect(damaged.storageNotice == nil && !damaged.hasUnfinishedSession, "Explicit reset can recover from unreadable storage")

        let blockedParent = directory.appendingPathComponent("a-file")
        try Data("not-a-directory".utf8).write(to: blockedParent)
        let unsaved = MathBuddyStore(storageURL: blockedParent.appendingPathComponent("save.json"))
        unsaved.startOrResume()
        expect(unsaved.storageNotice != nil && unsaved.round != nil, "A write error is visible and does not crash play")
        print("PASS: native round rules, two-stage subtraction, undo, assistance evidence, 3/5-round sessions, atomic resume, idempotent rewards, and storage failures")
    }

    @MainActor
    private static func finishRound(_ store: MathBuddyStore) {
        guard let round = store.round else { fatalError("Missing current round") }
        switch round.kind {
        case .counting:
            for id in 0..<round.countTarget { store.toggleObject(id) }
            store.checkCount()
        case .addition:
            store.joinGroups()
            store.chooseAnswer(round.answer)
        case .subtraction:
            for id in 0..<round.takeAway { store.toggleObject(id) }
            store.checkTransfer()
            store.chooseAnswer(round.answer)
        }
        expect(store.round?.phase == .success, "Authored round can be completed")
    }

    private static func expect(_ condition: @autoclosure () -> Bool, _ message: String) {
        precondition(condition(), message)
    }
}
