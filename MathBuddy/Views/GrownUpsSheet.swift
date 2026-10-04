import SwiftUI
import LocalAuthentication

struct GrownUpsSheet: View {
    let store: MathBuddyStore
    let audio: MathBuddyAudio
    @Environment(\.dismiss) private var dismiss
    @State private var isUnlocked = false
    @State private var isAuthenticating = false
    @State private var authenticationAvailable = false
    @State private var authenticationMessage: String?

    var body: some View {
        NavigationStack {
            Group {
                if isUnlocked {
                    GrownUpsView(store: store, audio: audio)
                } else {
                    adultGate
                }
            }
            .navigationTitle("Grown-ups")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Done") { dismiss() }
                        .fontWeight(.bold)
                }
            }
            .toolbarBackground(Storybook.cream, for: .navigationBar)
            .background(Storybook.cream)
        }
        .tint(Storybook.forest)
        .onAppear {
            let context = LAContext()
            authenticationAvailable = context.canEvaluatePolicy(.deviceOwnerAuthentication, error: nil)
            if !authenticationAvailable {
                authenticationMessage = "Set up a device passcode in iPad Settings to protect grown-up controls."
            }
        }
    }

    private var adultGate: some View {
        ScrollView {
            VStack(spacing: 24) {
                Image(systemName: "lock.shield")
                    .font(.system(size: 54, weight: .light))
                    .foregroundStyle(Storybook.forest)
                    .padding(.top, 60)
                    .accessibilityHidden(true)
                Text("A moment for a grown-up.")
                    .font(.system(.largeTitle, design: .rounded, weight: .bold))
                    .multilineTextAlignment(.center)
                Text("Use this iPad’s Face ID, Touch ID, or passcode to see progress and change settings.")
                    .font(.body)
                    .foregroundStyle(Storybook.muted)
                    .multilineTextAlignment(.center)

                if let authenticationMessage {
                    Text(authenticationMessage)
                        .foregroundStyle(Storybook.muted)
                        .multilineTextAlignment(.center)
                }

                Button(isAuthenticating ? "Unlocking…" : "Unlock grown-up controls", action: authenticate)
                    .buttonStyle(StoryButtonStyle())
                    .disabled(isAuthenticating || !authenticationAvailable)

                #if DEBUG && targetEnvironment(simulator)
                if !authenticationAvailable {
                    Button("Simulator review") { isUnlocked = true }
                        .buttonStyle(StoryButtonStyle(primary: false))
                        .accessibilityIdentifier("simulatorReviewButton")
                    Text("Development build only. This review entry is absent from Release builds.")
                        .font(.footnote)
                        .foregroundStyle(Storybook.muted)
                        .multilineTextAlignment(.center)
                }
                #endif
            }
            .frame(maxWidth: 570)
            .padding(32)
            .frame(maxWidth: .infinity)
        }
    }

    private func authenticate() {
        guard !isAuthenticating else { return }
        isAuthenticating = true
        authenticationMessage = nil
        Task { @MainActor in
            let context = LAContext()
            context.localizedCancelTitle = "Back to Pip"
            do {
                isUnlocked = try await context.evaluatePolicy(.deviceOwnerAuthentication, localizedReason: "Open MathBuddy’s grown-up settings and learning progress.")
            } catch {
                authenticationMessage = "Controls stayed locked. You can try again when you’re ready."
            }
            isAuthenticating = false
        }
    }
}

private struct GrownUpsView: View {
    let store: MathBuddyStore
    let audio: MathBuddyAudio
    @Environment(\.dismiss) private var dismiss
    @State private var confirmsReset = false
    @State private var confirmsRestart = false

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 24) {
                VStack(alignment: .leading, spacing: 8) {
                    Eyebrow(text: "Little steps, real understanding")
                    Text("Room to learn at their pace.")
                        .font(.system(.largeTitle, design: .rounded, weight: .black))
                    Text("Progress stays on this iPad. Help is always welcome, and never costs a reward.")
                        .foregroundStyle(Storybook.muted)
                }

                if let notice = store.storageNotice {
                    StoryPanel {
                        Label(notice, systemImage: "externaldrive.badge.exclamationmark")
                            .foregroundStyle(Storybook.forest)
                    }
                }

                progressPanel
                playSettings
                soundSettings
                sessionSettings

                StoryPanel {
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Bring a little math into the day")
                            .font(.system(.title3, design: .rounded, weight: .bold))
                        Text("At snack time, ask: “Can you put three pieces on my plate?” Let your child move the pieces and explain what they notice.")
                            .foregroundStyle(Storybook.muted)
                    }
                }
            }
            .frame(maxWidth: 800)
            .padding(28)
            .frame(maxWidth: .infinity)
        }
        .foregroundStyle(Storybook.forest)
        .background(Storybook.cream)
        .confirmationDialog("Clear all local progress?", isPresented: $confirmsReset, titleVisibility: .visible) {
            Button("Clear progress and garden", role: .destructive) { store.resetProgress() }
        } message: {
            Text("This removes this iPad’s saved rounds, learning history, and earned garden items. It cannot be undone.")
        }
        .confirmationDialog("Restart the unfinished adventure?", isPresented: $confirmsRestart, titleVisibility: .visible) {
            Button("Start a fresh adventure", role: .destructive) {
                store.newSession()
                dismiss()
            }
        } message: {
            Text("Only the unfinished session is replaced. Completed practice and earned garden items remain.")
        }
    }

    private var progressPanel: some View {
        StoryPanel {
            VStack(alignment: .leading, spacing: 20) {
                HStack {
                    Text("Our little discoveries")
                        .font(.system(.title2, design: .rounded, weight: .bold))
                    Spacer(minLength: 8)
                    Image(systemName: "leaf").foregroundStyle(Storybook.forest)
                }
                Text("\(store.inventory.completedSessions) adventures completed")
                    .font(.headline)
                ForEach(ActivityKind.allCases) { kind in
                    let stats = store.stats[kind] ?? ActivityStats()
                    VStack(alignment: .leading, spacing: 6) {
                        Text(kind.title).font(.headline)
                        Text(stats.completed == 0 ? "Ready to explore together." : "\(stats.withoutHelp) completed without extra help · \(stats.withHelp) with help")
                            .font(.subheadline)
                            .foregroundStyle(Storybook.muted)
                    }
                    .accessibilityElement(children: .combine)
                }
                Text("These are completed activities, not a score or a claim of mastery. Berries and other built-in supports are part of every activity.")
                    .font(.footnote)
                    .foregroundStyle(Storybook.muted)
            }
        }
    }

    private var playSettings: some View {
        StoryPanel {
            VStack(alignment: .leading, spacing: 20) {
                Text("A just-right adventure")
                    .font(.system(.title2, design: .rounded, weight: .bold))
                Picker("Practice", selection: setting(\.practiceMode)) {
                    Text("Counting first").tag(PracticeMode.counting)
                    Text("Count, join, and share").tag(PracticeMode.mixed)
                }
                .pickerStyle(.menu)
                .frame(minHeight: 54)
                Picker("Little jobs each time", selection: setting(\.sessionLength)) {
                    Text("3 little jobs").tag(3)
                    Text("5 little jobs").tag(5)
                }
                .pickerStyle(.segmented)
                .accessibilityLabel("Little jobs per adventure")
                Text("Changes apply to the next adventure. Counting first starts with three berries; mixed play includes joining and taking away within five.")
                    .font(.footnote)
                    .foregroundStyle(Storybook.muted)
            }
        }
    }

    private var soundSettings: some View {
        StoryPanel {
            VStack(alignment: .leading, spacing: 18) {
                Text("Make it comfortable")
                    .font(.system(.title2, design: .rounded, weight: .bold))
                Toggle("Spoken instructions", isOn: setting(\.narration))
                    .disabled(!audio.availableNarration)
                if !audio.availableNarration {
                    Text("Narration recordings are not bundled in this build. All instructions are visible on screen.")
                        .font(.footnote)
                        .foregroundStyle(Storybook.muted)
                }
                Toggle("Gentle sound effects", isOn: setting(\.effects))
                Toggle("Less movement", isOn: setting(\.reducedMotion))
                Text("The iPad’s Reduce Motion setting is always respected. Less movement also removes the spinning and spring effects.")
                    .font(.footnote)
                    .foregroundStyle(Storybook.muted)
            }
            .toggleStyle(.switch)
            .onChange(of: store.settings.narration) { audio.stop() }
            .onChange(of: store.settings.effects) { audio.stop() }
        }
    }

    private var sessionSettings: some View {
        StoryPanel {
            VStack(alignment: .leading, spacing: 14) {
                Text("Saved on this iPad")
                    .font(.system(.title2, design: .rounded, weight: .bold))
                Text(store.hasUnfinishedSession ? "An adventure is ready to continue from the home screen." : "No unfinished adventure. A fresh one begins from home.")
                    .foregroundStyle(Storybook.muted)
                if store.hasUnfinishedSession {
                    Button("Restart unfinished adventure") { confirmsRestart = true }
                        .frame(minHeight: 48)
                }
                Button("Clear local progress", role: .destructive) { confirmsReset = true }
                    .frame(minHeight: 48)
            }
        }
    }

    private func setting<Value>(_ keyPath: WritableKeyPath<ParentSettings, Value>) -> Binding<Value> {
        Binding {
            store.settings[keyPath: keyPath]
        } set: { value in
            var settings = store.settings
            settings[keyPath: keyPath] = value
            store.updateSettings(settings)
        }
    }
}
