import Foundation

/// Authored rendering inputs. These fixtures do not exercise touch or accessibility UI.
@main
struct ReviewFixtureBuilder {
    @MainActor
    static func main() throws {
        let manager = FileManager.default
        let output = URL(fileURLWithPath: CommandLine.arguments.dropFirst().first ?? "output/native/fixtures",
                         isDirectory: true)
        let temporary = manager.temporaryDirectory.appendingPathComponent("MathBuddy-fixtures-\(UUID().uuidString)")
        try manager.createDirectory(at: temporary, withIntermediateDirectories: true)
        defer { try? manager.removeItem(at: temporary) }
        try manager.createDirectory(at: output, withIntermediateDirectories: true)
        let source = temporary.appendingPathComponent("source.json")
        let store = MathBuddyStore(storageURL: source)
        var manifest: [[String: Any]] = []

        func capture(_ name: String) throws {
            store.save()
            guard store.storageNotice == nil else { throw FixtureError.failedSave }
            let data = try Data(contentsOf: source)
            let validationURL = temporary.appendingPathComponent("\(name)-validation.json")
            try data.write(to: validationURL, options: .atomic)
            let restored = MathBuddyStore(storageURL: validationURL)
            guard restored.storageNotice == nil, restored.route == store.route,
                  restored.round?.kind == store.round?.kind,
                  restored.round?.phase == store.round?.phase,
                  restored.round?.selected == store.round?.selected,
                  restored.stats == store.stats,
                  restored.inventory.completedSessions == store.inventory.completedSessions,
                  restored.inventory.pinwheelPlaced == store.inventory.pinwheelPlaced
            else { throw FixtureError.invalidRoundTrip }
            try data.write(to: output.appendingPathComponent("\(name).json"), options: .atomic)
            var item: [String: Any] = [
                "file": "\(name).json", "route": restored.route.rawValue,
                "completedSessions": restored.inventory.completedSessions,
                "pinwheelPlaced": restored.inventory.pinwheelPlaced
            ]
            if let round = restored.round {
                item["kind"] = round.kind.rawValue
                item["phase"] = round.phase.rawValue
                item["selectedObjectIDs"] = round.selected.sorted()
            }
            manifest.append(item)
        }

        try capture("home")
        store.startOrResume()
        store.toggleObject(0)
        store.toggleObject(2)
        try capture("count-partial")
        for id in [1, 3, 4] { store.toggleObject(id) }
        store.checkCount()
        try capture("count-success")
        store.advance()
        try capture("addition-before")
        store.joinGroups()
        try capture("addition-after")
        store.chooseAnswer(3)
        store.advance()
        try capture("subtraction-before")
        store.toggleObject(0)
        store.toggleObject(4)
        store.checkTransfer()
        try capture("subtraction-after")
        store.chooseAnswer(3)
        store.advance()
        try capture("garden-unplaced")
        store.placePinwheel()
        try capture("garden-placed")
        store.finishForNow()
        try capture("goodbye")

        let report: [String: Any] = [
            "evidence": "Saved-state fixture inputs for native Simulator render checks; not touch UI testing",
            "source": "Real MathBuddyStore actions in temporary isolated storage; no user data",
            "fixtureCount": manifest.count,
            "fixtures": manifest
        ]
        try JSONSerialization.data(withJSONObject: report, options: [.prettyPrinted, .sortedKeys])
            .write(to: output.appendingPathComponent("manifest.json"), options: .atomic)
        let readme = """
        # Native rendering fixtures

        These ten saved-state inputs are produced by real MathBuddyStore methods in isolated temporary storage.
        They contain no user data. Answers, object placement, phases, statistics, and rewards result from real
        model transitions. UUIDs and timestamps are produced by the store. Each fixture is reloaded through
        MathBuddyStore and compared before export; authored scene states are repeatable.

        Loading a fixture and capturing its native screen proves rendering of that saved state. It does not
        demonstrate taps, dragging, audio, animation timing, accessibility interaction, or a complete UI flow.
        Screenshots made from these files must be described as fixture-based native render checks.

        Regenerate from the repository root:

        ```sh
        swiftc -swift-version 6 -parse-as-library MathBuddy/Model/MathBuddyModels.swift MathBuddy/Model/MathBuddyStore.swift scripts/make-review-fixtures.swift -o /tmp/mathbuddy-review-fixtures
        /tmp/mathbuddy-review-fixtures output/native/fixtures
        ```

        """
        try readme.write(to: output.appendingPathComponent("README.md"), atomically: true, encoding: .utf8)
        print("PASS: \(manifest.count) native rendering fixtures; each reloaded and validated. No touch UI testing performed.")
    }

    private enum FixtureError: Error {
        case failedSave, invalidRoundTrip
    }
}
