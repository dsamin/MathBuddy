import SwiftUI

struct MathBuddyRootView: View {
    let store: MathBuddyStore
    let audio: MathBuddyAudio
    @Environment(\.accessibilityReduceMotion) private var systemReducedMotion
    @Environment(\.scenePhase) private var scenePhase
    @State private var showsGrownUps = false

    var body: some View {
        GeometryReader { proxy in
            ScrollView {
                Group {
                    switch store.route {
                    case .home:
                        HomeView(store: store, wide: proxy.size.width > 850) {
                            audio.stop()
                            showsGrownUps = true
                        }
                    case .activity:
                        if let round = store.round {
                            ActivityView(store: store, audio: audio, round: round, availableWidth: proxy.size.width - 64)
                                .id(round.id)
                        }
                    case .garden:
                        GardenView(store: store, audio: audio, wide: proxy.size.width > 850)
                    case .goodbye:
                        GoodbyeView(store: store)
                    }
                }
                .frame(maxWidth: 1180)
                .frame(minHeight: max(0, proxy.size.height - 56))
                .frame(maxWidth: .infinity)
                .padding(.horizontal, proxy.size.width < 600 ? 20 : 36)
                .padding(.vertical, 28)
            }
            .scrollBounceBehavior(.basedOnSize)
            .background(Storybook.cream.ignoresSafeArea())
            .foregroundStyle(Storybook.forest)
        }
        .fontDesign(.rounded)
        .environment(\.effectiveReduceMotion, systemReducedMotion || store.settings.reducedMotion)
        .sheet(isPresented: $showsGrownUps) {
            GrownUpsSheet(store: store, audio: audio)
                .presentationDetents([.large])
        }
        .onChange(of: store.route, initial: true) {
            switch store.route {
            case .home:
                audio.stop()
                audio.playNarration("welcome", enabled: store.settings.narration)
            case .garden:
                audio.stop()
                if store.inventory.ownsPinwheel && !store.inventory.pinwheelPlaced {
                    audio.playNarration("garden", enabled: store.settings.narration)
                }
            case .goodbye:
                audio.stop()
                audio.playNarration("goodbye", enabled: store.settings.narration)
            case .activity: break
            }
        }
        .onChange(of: scenePhase) {
            if scenePhase != .active {
                audio.stop()
                store.save()
            }
            if scenePhase == .background {
                showsGrownUps = false
            }
        }
    }
}

struct HomeView: View {
    let store: MathBuddyStore
    let wide: Bool
    let openGrownUps: () -> Void
    @ScaledMetric(relativeTo: .largeTitle) private var titleSize = 51.0
    @Environment(\.dynamicTypeSize) private var dynamicTypeSize

    private var sideBySide: Bool { wide && !dynamicTypeSize.isAccessibilitySize }

    var body: some View {
        VStack(spacing: sideBySide ? 48 : 28) {
            ViewThatFits(in: .horizontal) {
                HStack {
                    BrandMark()
                    Spacer(minLength: 16)
                    adultButton
                }
                VStack(alignment: .leading, spacing: 16) {
                    BrandMark()
                    adultButton
                }
            }

            let layout = sideBySide ? AnyLayout(HStackLayout(alignment: .center, spacing: 38)) : AnyLayout(VStackLayout(spacing: 28))
            layout {
                welcomeCopy
                    .frame(maxWidth: .infinity, alignment: .leading)
                WelcomeIllustration()
                    .frame(maxWidth: sideBySide ? 530 : 600)
                    .frame(height: sideBySide ? 440 : 330)
            }
            .frame(maxWidth: .infinity)
            .padding(.vertical, sideBySide ? 10 : 0)

            HStack(alignment: .center) {
                Label("A little play. A little discovery.", systemImage: "leaf")
                Spacer(minLength: 16)
                if sideBySide { Text("COUNT · WONDER · GROW").tracking(1.5) }
            }
            .font(.system(.footnote, design: .rounded))
            .foregroundStyle(Storybook.muted)
        }
    }

    private var adultButton: some View {
        Button(action: openGrownUps) {
            Label("Grown-ups", systemImage: "lock")
        }
        .buttonStyle(StoryButtonStyle(primary: false, compact: true))
        .accessibilityIdentifier("grownUpsButton")
    }

    private var welcomeCopy: some View {
        VStack(alignment: .leading, spacing: 24) {
            Eyebrow(text: "A berry nice day")
            VStack(alignment: .leading, spacing: 1) {
                Text("Little numbers.").foregroundStyle(Storybook.forest)
                Text("Big adventures.").foregroundStyle(Storybook.coral)
            }
            .font(.system(size: titleSize, weight: .black, design: .rounded))
            .fixedSize(horizontal: false, vertical: true)
            .accessibilityElement(children: .combine)

            Text("Let’s make something\nwonderful with Pip.")
                .font(.system(.title3, design: .rounded))
                .foregroundStyle(Storybook.muted)
                .lineSpacing(5)
                .fixedSize(horizontal: false, vertical: true)

            VStack(alignment: .leading, spacing: 14) {
                Button(action: store.startOrResume) {
                    Label(store.hasUnfinishedSession ? "Keep playing with Pip" : "Play with Pip", systemImage: "arrow.right")
                        .labelStyle(TrailingIconLabelStyle())
                }
                .buttonStyle(StoryButtonStyle())
                .accessibilityIdentifier("playButton")

                Button(action: store.openGarden) {
                    Label("My garden", systemImage: "leaf")
                }
                .buttonStyle(StoryButtonStyle(primary: false))
                .accessibilityIdentifier("gardenButton")
            }
        }
    }
}

struct TrailingIconLabelStyle: LabelStyle {
    func makeBody(configuration: Configuration) -> some View {
        HStack(spacing: 18) {
            configuration.title
            configuration.icon
        }
    }
}

struct WelcomeIllustration: View {
    var body: some View {
        GeometryReader { proxy in
            ZStack(alignment: .bottom) {
                Image(decorative: "GardenBackground")
                    .resizable()
                    .scaledToFill()
                    .frame(width: proxy.size.width, height: proxy.size.height)
                    .clipped()
                LinearGradient(colors: [.clear, Storybook.sage.opacity(0.2)], startPoint: .center, endPoint: .bottom)
                Image(decorative: "PipWelcome")
                    .resizable()
                    .scaledToFit()
                    .frame(height: proxy.size.height * 0.8)
                    .padding(.bottom, 8)
                    .offset(x: proxy.size.width * 0.08)
                Text("Hi, friend!")
                    .font(.system(.title3, design: .rounded, weight: .black))
                    .padding(.horizontal, 22)
                    .padding(.vertical, 15)
                    .background(Storybook.paper, in: RoundedRectangle(cornerRadius: 22))
                    .rotationEffect(.degrees(4))
                    .position(x: proxy.size.width * 0.72, y: proxy.size.height * 0.16)
            }
            .clipShape(UnevenRoundedRectangle(topLeadingRadius: 140, bottomLeadingRadius: 34, bottomTrailingRadius: 34, topTrailingRadius: 140))
        }
        .accessibilityHidden(true)
    }
}

struct GoodbyeView: View {
    let store: MathBuddyStore

    var body: some View {
        VStack(spacing: 28) {
            Image(decorative: "PipHappy")
                .resizable()
                .scaledToFit()
                .frame(maxWidth: 320, maxHeight: 320)
            Eyebrow(text: "A little play. A lovely day.")
            Text("See you soon, friend.")
                .font(.system(.largeTitle, design: .rounded, weight: .black))
                .multilineTextAlignment(.center)
            Text("Your garden will be here when you’re ready.")
                .font(.system(.title3, design: .rounded))
                .multilineTextAlignment(.center)
                .foregroundStyle(Storybook.muted)
            Button("Back home", action: store.goHome)
                .buttonStyle(StoryButtonStyle(primary: false))
        }
        .padding(.vertical, 24)
    }
}
