import Foundation

enum AppRoute: String, Codable, Equatable {
    case home, activity, garden, goodbye
}

enum ActivityKind: String, Codable, CaseIterable, Identifiable {
    case counting, addition, subtraction

    var id: String { rawValue }
    var title: String {
        switch self {
        case .counting: "Making a group"
        case .addition: "Joining groups"
        case .subtraction: "Taking away"
        }
    }
}

enum PracticeMode: String, Codable, CaseIterable, Identifiable {
    case counting, mixed
    var id: String { rawValue }
}

enum RoundPhase: String, Codable, Equatable {
    case interacting, answering, success
}

struct ParentSettings: Codable, Equatable {
    var narration = true
    var effects = true
    var reducedMotion = false
    var sessionLength = 3
    var practiceMode: PracticeMode = .mixed
}

struct ActivityStats: Codable, Equatable {
    var completed = 0
    var withHelp = 0
    var withoutHelp: Int { completed - withHelp }
}

struct GardenInventory: Codable, Equatable {
    var completedSessionIDs: Set<UUID> = []
    var pinwheelPlaced = false
    var ownsPinwheel: Bool { !completedSessionIDs.isEmpty }
    var completedSessions: Int { completedSessionIDs.count }
}

struct RoundState: Codable, Equatable, Identifiable {
    let id: UUID
    let contentID: String
    let kind: ActivityKind
    let total: Int
    let countTarget: Int
    let addLeft: Int
    let addRight: Int
    let takeAway: Int
    let answerOptions: [Int]
    var phase: RoundPhase = .interacting
    var selected: Set<Int> = []
    var moveHistory: [Set<Int>] = []
    var feedback: String?
    var helpUsed = false
    var submittedAnswers = 0
    var incorrectSubmissions = 0
    var firstSubmissionCorrect: Bool?
    var completedAt: Date?

    // IDs describe the immutable authored set, never an object's current position.
    var objectIDs: [Int] { Array(0..<total) }
    var isJoined: Bool { kind == .addition && phase != .interacting }
    var answer: Int {
        switch kind {
        case .counting: countTarget
        case .addition: addLeft + addRight
        case .subtraction: total - takeAway
        }
    }

    var instruction: String {
        switch kind {
        case .counting:
            "Pack \(countTarget) berries for Pip."
        case .addition:
            phase == .interacting
                ? "\(addLeft) berries. \(addRight) more joins."
                : "How many berries altogether?"
        case .subtraction:
            phase == .interacting
                ? "Give \(takeAway) berries to our friend."
                : "How many berries are left here?"
        }
    }

    var successEquation: String {
        switch kind {
        case .counting: "\(countTarget) berries for Pip!"
        case .addition: "\(addLeft) + \(addRight) = \(answer)"
        case .subtraction: "\(total) − \(takeAway) = \(answer)"
        }
    }

    static func counting(target: Int, available: Int, contentID: String) -> Self {
        Self(id: UUID(), contentID: contentID, kind: .counting, total: available,
             countTarget: target, addLeft: 0, addRight: 0, takeAway: 0, answerOptions: [])
    }

    static func addition(left: Int, right: Int, contentID: String, options: [Int]) -> Self {
        Self(id: UUID(), contentID: contentID, kind: .addition, total: left + right,
             countTarget: 0, addLeft: left, addRight: right, takeAway: 0, answerOptions: options)
    }

    static func subtraction(total: Int, takeAway: Int, contentID: String, options: [Int]) -> Self {
        Self(id: UUID(), contentID: contentID, kind: .subtraction, total: total,
             countTarget: 0, addLeft: 0, addRight: 0, takeAway: takeAway, answerOptions: options)
    }

    var isValid: Bool {
        guard (0...10).contains(total), (0...total).contains(countTarget),
              (0...total).contains(takeAway), submittedAnswers >= 0,
              (0...submittedAnswers).contains(incorrectSubmissions),
              selected.allSatisfy({ (0..<total).contains($0) }),
              moveHistory.allSatisfy({ $0.allSatisfy { (0..<total).contains($0) } }),
              (phase == .success) == (completedAt != nil) else { return false }
        switch kind {
        case .counting:
            return phase != .answering && (phase != .success || selected.count == countTarget)
        case .addition:
            return (0...total).contains(addLeft) && (0...total).contains(addRight)
                && addLeft + addRight == total && validOptions
        case .subtraction:
            return validOptions && (phase == .interacting || selected.count == takeAway)
        }
    }

    private var validOptions: Bool {
        answerOptions.count == 3 && Set(answerOptions).count == answerOptions.count
            && answerOptions.contains(answer) && answerOptions.allSatisfy { (0...10).contains($0) }
    }
}

struct SessionCheckpoint: Codable, Equatable, Identifiable {
    let id: UUID
    var rounds: [RoundState]
    var currentIndex = 0
    var completedAt: Date?

    var isComplete: Bool { completedAt != nil }

    static func authored(settings: ParentSettings) -> Self {
        var rounds: [RoundState]
        if settings.practiceMode == .counting {
            rounds = [
                .counting(target: 3, available: 5, contentID: "count-3-of-5"),
                .counting(target: 5, available: 6, contentID: "count-5-of-6"),
                .counting(target: 3, available: 4, contentID: "count-3-of-4")
            ]
            if settings.sessionLength == 5 {
                rounds += [
                    .counting(target: 5, available: 7, contentID: "count-5-of-7"),
                    .counting(target: 3, available: 5, contentID: "count-3-of-5-repeat")
                ]
            }
        } else {
            rounds = [
                .counting(target: 5, available: 6, contentID: "count-5-of-6"),
                .addition(left: 2, right: 1, contentID: "join-2-and-1", options: [4, 2, 3]),
                .subtraction(total: 5, takeAway: 2, contentID: "share-2-from-5", options: [3, 4, 2])
            ]
            if settings.sessionLength == 5 {
                rounds += [
                    .counting(target: 3, available: 5, contentID: "count-3-of-5"),
                    .addition(left: 1, right: 2, contentID: "join-1-and-2", options: [2, 3, 4])
                ]
            }
        }
        return Self(id: UUID(), rounds: rounds)
    }

    var isValid: Bool {
        [3, 5].contains(rounds.count) && rounds.indices.contains(currentIndex)
            && Set(rounds.map(\.id)).count == rounds.count
            && rounds.allSatisfy(\.isValid)
            && rounds.prefix(currentIndex).allSatisfy { $0.phase == .success }
            && (!isComplete || rounds.allSatisfy { $0.phase == .success })
    }
}

struct SavedProgress: Codable {
    var version = 1
    var route: AppRoute
    var settings: ParentSettings
    var inventory: GardenInventory
    var stats: [ActivityKind: ActivityStats]
    var session: SessionCheckpoint?

    var isValid: Bool {
        let completedSessionIsGranted = session.map {
            !$0.isComplete || inventory.completedSessionIDs.contains($0.id)
        } ?? true
        return version == 1 && [3, 5].contains(settings.sessionLength)
            && stats.values.allSatisfy { $0.completed >= 0 && (0...$0.completed).contains($0.withHelp) }
            && (session?.isValid ?? true)
            && (route != .activity || (session != nil && session?.isComplete == false))
            && (!inventory.pinwheelPlaced || inventory.ownsPinwheel)
            && completedSessionIsGranted
    }
}
