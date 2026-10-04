import SwiftUI

private struct EffectiveReduceMotionKey: EnvironmentKey {
    static let defaultValue = false
}

extension EnvironmentValues {
    var effectiveReduceMotion: Bool {
        get { self[EffectiveReduceMotionKey.self] }
        set { self[EffectiveReduceMotionKey.self] = newValue }
    }
}

enum Storybook {
    static let cream = Color(red: 1, green: 0.976, blue: 0.925)
    static let forest = Color(red: 0.137, green: 0.302, blue: 0.224)
    static let coral = Color(red: 0.851, green: 0.365, blue: 0.278)
    static let sage = Color(red: 0.843, green: 0.886, blue: 0.800)
    static let butter = Color(red: 0.965, green: 0.849, blue: 0.533)
    static let sky = Color(red: 0.808, green: 0.902, blue: 0.886)
    static let muted = Color(red: 0.365, green: 0.408, blue: 0.325)
    static let paper = Color(red: 1, green: 0.992, blue: 0.973)
    static let wood = Color(red: 0.714, green: 0.486, blue: 0.278)
}

struct StoryButtonStyle: ButtonStyle {
    var primary = true
    var compact = false
    @Environment(\.effectiveReduceMotion) private var reduceMotion
    @Environment(\.isEnabled) private var isEnabled

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.system(compact ? .headline : .title3, design: .rounded, weight: .bold))
            .multilineTextAlignment(.center)
            .padding(.horizontal, compact ? 20 : 30)
            .padding(.vertical, 16)
            .frame(minHeight: 64)
            .foregroundStyle(primary ? Storybook.cream : Storybook.forest)
            .background(primary ? Storybook.forest : Storybook.paper, in: RoundedRectangle(cornerRadius: 23))
            .overlay {
                RoundedRectangle(cornerRadius: 23)
                    .strokeBorder(Storybook.forest.opacity(primary ? 0 : 0.15), lineWidth: 1.5)
            }
            .shadow(color: Storybook.forest.opacity(primary ? 0.12 : 0.03), radius: 0, y: configuration.isPressed ? 0 : 4)
            .opacity(isEnabled ? 1 : 0.45)
            .scaleEffect(configuration.isPressed && !reduceMotion ? 0.975 : 1)
            .animation(reduceMotion ? nil : .easeOut(duration: 0.12), value: configuration.isPressed)
    }
}

struct Eyebrow: View {
    let text: String

    var body: some View {
        Text(text.uppercased())
            .font(.system(.caption, design: .rounded, weight: .heavy))
            .tracking(2)
            .foregroundStyle(Storybook.muted)
            .fixedSize(horizontal: false, vertical: true)
    }
}

struct RoundProgressView: View {
    let current: Int
    let total: Int

    var body: some View {
        HStack(spacing: 10) {
            ForEach(1...max(1, total), id: \.self) { step in
                Capsule()
                    .fill(step <= current ? Storybook.coral : Storybook.forest.opacity(0.13))
                    .frame(width: step == current ? 30 : 12, height: 12)
            }
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel("Little job \(current) of \(total)")
    }
}

struct StoryPanel<Content: View>: View {
    @ViewBuilder var content: Content

    var body: some View {
        content
            .padding(24)
            .background(Storybook.paper, in: RoundedRectangle(cornerRadius: 28))
            .overlay {
                RoundedRectangle(cornerRadius: 28)
                    .strokeBorder(Storybook.forest.opacity(0.09), lineWidth: 1)
            }
    }
}

struct BrandMark: View {
    var body: some View {
        HStack(spacing: 12) {
            Image(decorative: "PipWelcome")
                .resizable()
                .scaledToFit()
                .frame(width: 44, height: 56)
            VStack(alignment: .leading, spacing: 3) {
                Text("MathBuddy")
                    .font(.system(.title2, design: .rounded, weight: .black))
                Text("A LITTLE WORLD OF NUMBERS")
                    .font(.system(.caption2, design: .rounded, weight: .bold))
                    .tracking(1.2)
            }
        }
        .foregroundStyle(Storybook.forest)
        .accessibilityElement(children: .combine)
    }
}
