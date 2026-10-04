import SwiftUI

struct GardenView: View {
    let store: MathBuddyStore
    let audio: MathBuddyAudio
    let wide: Bool
    @Environment(\.effectiveReduceMotion) private var reduceMotion
    @State private var pinwheelRotation = 0.0
    @State private var flowerOpen = false
    @ScaledMetric(relativeTo: .largeTitle) private var headingSize = 38.0

    var body: some View {
        VStack(spacing: 25) {
            HStack {
                Button(action: store.goHome) {
                    Label("Home", systemImage: "house")
                }
                .buttonStyle(StoryButtonStyle(primary: false, compact: true))
                Spacer()
                Eyebrow(text: "My little garden")
            }

            VStack(spacing: 10) {
                Text(store.inventory.ownsPinwheel ? "Look what you helped grow." : "A little place of your own.")
                    .font(.system(size: headingSize, weight: .black, design: .rounded))
                    .multilineTextAlignment(.center)
                Text(gardenPrompt)
                    .font(.system(.title3, design: .rounded))
                    .foregroundStyle(Storybook.muted)
                    .multilineTextAlignment(.center)
            }

            gardenScene
                .frame(height: wide ? 350 : 380)

            if store.inventory.ownsPinwheel && !store.inventory.pinwheelPlaced {
                Button {
                    store.placePinwheel()
                    audio.playEffect("reward", enabled: store.settings.effects)
                } label: {
                    Label("Plant my pinwheel", systemImage: "leaf")
                }
                .buttonStyle(StoryButtonStyle())
                .accessibilityIdentifier("placePinwheelButton")
            }

            ViewThatFits(in: .horizontal) {
                HStack(spacing: 18) { gardenActions }
                VStack(spacing: 18) { gardenActions }
            }
        }
    }

    private var gardenPrompt: String {
        if store.inventory.ownsPinwheel && !store.inventory.pinwheelPlaced { return "Your pinwheel is ready. Let’s give it a home." }
        if store.inventory.pinwheelPlaced { return "Tap your pinwheel for a little breeze." }
        return "Tap the flower. There’s always something to play with here."
    }

    @ViewBuilder private var gardenActions: some View {
        Button("Done for today", action: store.finishForNow)
            .buttonStyle(StoryButtonStyle(primary: false))
            .accessibilityIdentifier("doneForTodayButton")
        Button(store.hasUnfinishedSession ? "Keep playing" : "Play again", action: store.startOrResume)
            .buttonStyle(StoryButtonStyle(primary: false))
            .accessibilityIdentifier("playAgainButton")
    }

    private var gardenScene: some View {
        GeometryReader { proxy in
            ZStack {
                Image(decorative: "GardenBackground")
                    .resizable()
                    .scaledToFill()
                    .frame(width: proxy.size.width, height: proxy.size.height)
                    .clipped()
                Image(decorative: "PipHappy")
                    .resizable()
                    .scaledToFit()
                    .frame(height: proxy.size.height * 0.62)
                    .position(x: proxy.size.width * 0.73, y: proxy.size.height * 0.68)

                if store.inventory.pinwheelPlaced {
                    Button(action: spinPinwheel) {
                        PinwheelView(rotation: pinwheelRotation)
                            .frame(width: 150, height: 225)
                            .padding(8)
                            .contentShape(Rectangle())
                    }
                    .buttonStyle(.plain)
                    .position(x: proxy.size.width * 0.32, y: proxy.size.height * 0.59)
                    .accessibilityLabel("My pinwheel")
                    .accessibilityHint(reduceMotion ? "Tap to turn the pinwheel a little" : "Tap to spin the pinwheel")
                    .accessibilityIdentifier("pinwheelButton")
                }

                ForEach(0..<min(24, max(0, store.inventory.completedSessions - 1)), id: \.self) { flower in
                    LittleFlower(color: flower.isMultiple(of: 2) ? Storybook.coral : Storybook.butter)
                        .scaleEffect(0.8)
                        .position(x: proxy.size.width * (0.12 + CGFloat(flower % 8) * 0.1), y: proxy.size.height * (0.91 - CGFloat(flower / 8) * 0.11))
                }

                Button {
                    withAnimation(reduceMotion ? nil : .spring(response: 0.4, dampingFraction: 0.6)) { flowerOpen.toggle() }
                    audio.playEffect("pickup", enabled: store.settings.effects)
                } label: {
                    LittleFlower(color: flowerOpen ? Storybook.butter : Storybook.coral)
                        .scaleEffect(flowerOpen && !reduceMotion ? 1.3 : 1)
                        .frame(width: 84, height: 84)
                        .contentShape(Circle())
                }
                .buttonStyle(.plain)
                .position(x: proxy.size.width * 0.16, y: proxy.size.height * 0.84)
                .accessibilityLabel("Garden flower")
                .accessibilityHint("Tap to change its color")
                .accessibilityIdentifier("gardenFlowerButton")
            }
            .clipShape(RoundedRectangle(cornerRadius: 40))
            .overlay { RoundedRectangle(cornerRadius: 40).strokeBorder(Storybook.forest.opacity(0.08), lineWidth: 1) }
        }
    }

    private func spinPinwheel() {
        withAnimation(reduceMotion ? nil : .easeOut(duration: 1.6)) {
            pinwheelRotation += reduceMotion ? 90 : 720
        }
        audio.playEffect("pickup", enabled: store.settings.effects)
    }
}
