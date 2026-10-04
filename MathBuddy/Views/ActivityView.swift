import SwiftUI

struct ActivityView: View {
    let store: MathBuddyStore
    let audio: MathBuddyAudio
    let round: RoundState
    let availableWidth: CGFloat
    @Environment(\.effectiveReduceMotion) private var reduceMotion
    @Environment(\.dynamicTypeSize) private var dynamicTypeSize
    @ScaledMetric(relativeTo: .largeTitle) private var promptSize = 36.0

    private var canListen: Bool { store.settings.narration && audio.availableNarration }
    private var isSuccess: Bool { round.phase == .success }
    private var movement: Animation? { reduceMotion ? nil : .spring(response: 0.38, dampingFraction: 0.78) }

    var body: some View {
        VStack(spacing: 24) {
            topBar
            VStack(spacing: 10) {
                Eyebrow(text: isSuccess ? "You made it happen" : chapterLabel)
                Text(isSuccess ? round.successEquation : round.instruction)
                    .font(.system(size: promptSize, weight: .black, design: .rounded))
                    .multilineTextAlignment(.center)
                    .fixedSize(horizontal: false, vertical: true)
                    .accessibilityAddTraits(.isHeader)
                Text(isSuccess ? "A little math. A lovely thing to share." : supportingPrompt)
                    .font(.system(.title3, design: .rounded))
                    .foregroundStyle(Storybook.muted)
                    .multilineTextAlignment(.center)
                    .fixedSize(horizontal: false, vertical: true)
            }

            BerryWorkspace(round: round, compact: availableWidth < 620, move: moveObject, playCount: playCount)
                .frame(height: availableWidth < 620 ? 545 : 300)
                .animation(movement, value: round.selected)
                .animation(movement, value: round.phase)

            if let feedback = round.feedback, !isSuccess {
                Text(feedback)
                    .font(.system(.headline, design: .rounded))
                    .foregroundStyle(Storybook.forest)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 20)
                    .padding(.vertical, 13)
                    .frame(maxWidth: 780)
                    .background(Storybook.sage.opacity(0.55), in: RoundedRectangle(cornerRadius: 18))
                    .accessibilityIdentifier("activityFeedback")
            }

            controls
        }
        .onAppear(perform: replayPrompt)
        .onChange(of: round.phase) {
            if isSuccess {
                audio.playEffect("success", enabled: store.settings.effects)
                audio.playNarration("success", enabled: store.settings.narration)
            } else {
                replayPrompt()
            }
        }
    }

    private var topBar: some View {
        HStack(spacing: 16) {
            Button {
                audio.stop()
                store.goHome()
            } label: {
                Image(systemName: "house")
                    .frame(minWidth: 22)
            }
            .buttonStyle(StoryButtonStyle(primary: false, compact: true))
            .accessibilityLabel("Pause and go home. Your work is saved.")
            .accessibilityIdentifier("activityHome")

            Spacer(minLength: 0)
            RoundProgressView(current: store.roundNumber, total: store.sessionRoundCount)
            Spacer(minLength: 0)

            Button(action: replayPrompt) {
                Label(canListen ? "Listen" : "Sound off", systemImage: canListen ? "speaker.wave.2" : "speaker.slash")
            }
            .buttonStyle(StoryButtonStyle(primary: false, compact: true))
            .disabled(!canListen)
            .accessibilityLabel(canListen ? "Listen to the instruction again" : "Spoken instructions are unavailable or switched off")
        }
    }

    @ViewBuilder private var controls: some View {
        if isSuccess {
            HStack(spacing: 18) {
                SuccessBuddyView()
                Button(store.roundNumber == store.sessionRoundCount ? "Visit my garden" : "Next little job") {
                    audio.stop()
                    store.advance()
                }
                .buttonStyle(StoryButtonStyle())
                .accessibilityIdentifier("continueButton")
            }
        } else {
            VStack(spacing: 18) {
                if round.phase == .answering {
                    let answerLayout = dynamicTypeSize.isAccessibilitySize || availableWidth < 330
                        ? AnyLayout(VStackLayout(spacing: 16))
                        : AnyLayout(HStackLayout(spacing: 16))
                    answerLayout {
                        ForEach(round.answerOptions, id: \.self) { answer in
                            Button {
                                store.chooseAnswer(answer)
                            } label: {
                                Text(answer, format: .number)
                                    .font(.system(.largeTitle, design: .rounded, weight: .black))
                                    .frame(minWidth: 40, minHeight: 48)
                            }
                            .buttonStyle(StoryButtonStyle(primary: false, compact: true))
                            .accessibilityLabel("\(answer) berries")
                            .accessibilityIdentifier("answer\(answer)")
                        }
                    }
                } else {
                    Button(primaryTitle, action: primaryAction)
                        .buttonStyle(StoryButtonStyle())
                        .accessibilityIdentifier("checkButton")
                }
                ViewThatFits(in: .horizontal) {
                    HStack(spacing: 16) { supportButtons }
                    VStack(spacing: 12) { supportButtons }
                }
            }
        }
    }

    @ViewBuilder private var supportButtons: some View {
        if (round.kind != .addition && round.phase == .interacting)
            || (round.kind == .addition && round.phase == .answering) {
            Button {
                withAnimation(movement) { store.undo() }
            } label: {
                Label("Undo", systemImage: "arrow.uturn.backward")
            }
            .buttonStyle(StoryButtonStyle(primary: false, compact: true))
            .disabled(!store.canUndo)
            .accessibilityIdentifier("undoButton")
        }
        Button {
            withAnimation(movement) { store.requestHelp() }
            audio.playNarration("help-count", enabled: store.settings.narration)
        } label: {
            Label("Help me", systemImage: "hand.raised")
        }
        .buttonStyle(StoryButtonStyle(primary: false, compact: true))
        .accessibilityIdentifier("helpButton")
    }

    private var chapterLabel: String {
        switch round.kind {
        case .counting: "A picnic for Pip"
        case .addition: "Friends bring snacks"
        case .subtraction: "A little something to share"
        }
    }

    private var supportingPrompt: String {
        switch round.kind {
        case .counting: "Tap a berry to pack it. Tap it again to put it back."
        case .addition:
            round.phase == .interacting ? "Let’s put the two groups together." : "Touch the berries to count, then choose a number."
        case .subtraction:
            round.phase == .interacting ? "Tap a berry to move it to our friend’s plate." : "Count the berries on the picnic mat, then choose."
        }
    }

    private var primaryTitle: String {
        switch round.kind {
        case .counting: "Done packing"
        case .addition: "Join the berries"
        case .subtraction: "Done sharing"
        }
    }

    private func primaryAction() {
        withAnimation(movement) {
            switch round.kind {
            case .counting: store.checkCount()
            case .addition: store.joinGroups()
            case .subtraction: store.checkTransfer()
            }
        }
    }

    private func moveObject(_ id: Int) {
        audio.playEffect("pickup", enabled: store.settings.effects)
        withAnimation(movement) { store.toggleObject(id) }
    }

    private func playCount() {
        audio.playEffect("pickup", enabled: store.settings.effects)
    }

    private func replayPrompt() {
        let key: String
        if isSuccess { key = "success" }
        else if round.phase == .answering { key = round.kind == .addition ? "choose-total" : "choose-remaining" }
        else {
            switch round.kind {
            case .counting: key = "count-\(round.countTarget)"
            case .addition: key = "add-\(round.addLeft)-\(round.addRight)"
            case .subtraction: key = "subtract-\(round.total)-\(round.takeAway)"
            }
        }
        audio.playNarration(key, enabled: store.settings.narration)
    }
}

private struct SuccessBuddyView: View {
    @Environment(\.effectiveReduceMotion) private var reduceMotion
    @State private var arrived = false

    var body: some View {
        ZStack {
            LittleFlower(color: Storybook.butter)
                .scaleEffect(0.38)
                .offset(x: -36, y: -24)
            Image(decorative: "PipHappy")
                .resizable()
                .scaledToFit()
                .frame(width: 72, height: 82)
            LittleFlower(color: Storybook.coral)
                .scaleEffect(0.3)
                .offset(x: 34, y: 27)
        }
        .frame(width: 94, height: 88)
        .scaleEffect(arrived || reduceMotion ? 1 : 0.82)
        .opacity(arrived || reduceMotion ? 1 : 0.5)
        .onAppear {
            withAnimation(reduceMotion ? nil : .spring(response: 0.48, dampingFraction: 0.7)) {
                arrived = true
            }
        }
        .accessibilityHidden(true)
    }
}

private struct BerryWorkspace: View {
    let round: RoundState
    let compact: Bool
    let move: (Int) -> Void
    let playCount: () -> Void
    @State private var touched: Set<Int> = []

    var body: some View {
        GeometryReader { proxy in
            let width = proxy.size.width
            let height = proxy.size.height
            ZStack {
                if round.kind == .addition {
                    additionMats(width: width, height: height)
                } else {
                    transferMats(width: width, height: height)
                }
                ForEach(round.objectIDs, id: \.self) { id in
                    berryButton(id)
                        .position(position(for: id, width: width, height: height))
                }
            }
        }
        .accessibilityElement(children: .contain)
        .accessibilityLabel(round.kind == .counting ? "Berry tray and picnic basket" : "Picnic workspace")
        .onChange(of: round.phase) {
            if round.phase == .interacting { touched.removeAll() }
        }
    }

    private func berryButton(_ id: Int) -> some View {
        let selected = round.selected.contains(id)
        let countOnly = round.phase == .answering
        return Button {
            if countOnly {
                if touched.contains(id) { touched.remove(id) } else { touched.insert(id) }
                playCount()
            } else {
                move(id)
            }
        } label: {
            StrawberryView()
                .frame(width: 68, height: 72)
                .frame(width: 82, height: 84)
                .background(touched.contains(id) ? Storybook.butter.opacity(0.7) : .clear, in: RoundedRectangle(cornerRadius: 22))
                .overlay {
                    if touched.contains(id) {
                        RoundedRectangle(cornerRadius: 22).strokeBorder(Storybook.forest.opacity(0.35), lineWidth: 2)
                    }
                }
                .contentShape(RoundedRectangle(cornerRadius: 22))
        }
        .buttonStyle(MathPieceButtonStyle())
        .disabled(round.phase == .success || (round.kind == .addition && round.phase == .interacting) || (round.kind == .subtraction && selected && countOnly))
        .opacity(round.kind == .subtraction && selected && countOnly ? 0.65 : 1)
        .accessibilityLabel(objectLabel(selected: selected, countOnly: countOnly))
        .accessibilityHint(countOnly ? "Tap to mark this berry while you count" : selected ? "Tap to put it back" : "Tap to move this berry")
        .accessibilityIdentifier("berry\(id)")
    }

    private func objectLabel(selected: Bool, countOnly: Bool) -> String {
        if round.kind == .counting { return selected ? "Berry in Pip’s basket" : "Berry on the tray" }
        if round.kind == .subtraction { return selected ? "Berry on our friend’s plate" : "Berry on the picnic mat" }
        return countOnly ? "Berry on the shared mat" : "Berry waiting to join"
    }

    @ViewBuilder private func transferMats(width: CGFloat, height: CGFloat) -> some View {
        let left = sourceCenter(width: width, height: height)
        let right = destinationCenter(width: width, height: height)
        let matWidth = compact ? min(width - 10, 420) : width * 0.53
        RoundedRectangle(cornerRadius: 44)
            .fill(Storybook.butter.opacity(0.25))
            .overlay { RoundedRectangle(cornerRadius: 44).strokeBorder(Storybook.wood.opacity(0.12), style: StrokeStyle(lineWidth: 2, dash: [5, 7])) }
            .frame(width: matWidth, height: 245)
            .position(left)
        Text(round.kind == .counting ? "THE BERRY TRAY" : "OUR PICNIC MAT")
            .font(.system(.caption2, design: .rounded, weight: .bold))
            .tracking(1.5)
            .foregroundStyle(Storybook.muted)
            .position(x: left.x, y: left.y + 101)
            .accessibilityHidden(true)
        if round.kind == .counting {
            BasketView()
                .frame(width: compact ? 270 : min(330, width * 0.4), height: 230)
                .position(x: right.x, y: right.y + 10)
        } else {
            Ellipse()
                .fill(Storybook.sky.opacity(0.68))
                .overlay { Ellipse().strokeBorder(Storybook.forest.opacity(0.14), lineWidth: 3) }
                .frame(width: compact ? 290 : width * 0.38, height: 226)
                .position(right)
            Text("OUR FRIEND’S PLATE")
                .font(.system(.caption2, design: .rounded, weight: .bold))
                .tracking(1.5)
                .foregroundStyle(Storybook.muted)
                .position(x: right.x, y: right.y + 90)
                .accessibilityHidden(true)
        }
    }

    @ViewBuilder private func additionMats(width: CGFloat, height: CGFloat) -> some View {
        if round.isJoined {
            RoundedRectangle(cornerRadius: 54)
                .fill(Storybook.sage.opacity(0.55))
                .frame(width: min(width - 12, 660), height: 245)
                .position(x: width / 2, y: height / 2)
        } else {
            RoundedRectangle(cornerRadius: 44)
                .fill(Storybook.butter.opacity(0.3))
                .frame(width: compact ? min(width - 12, 380) : width * 0.43, height: 230)
                .position(sourceCenter(width: width, height: height))
            RoundedRectangle(cornerRadius: 44)
                .fill(Storybook.sky.opacity(0.6))
                .frame(width: compact ? min(width - 12, 380) : width * 0.38, height: 230)
                .position(destinationCenter(width: width, height: height))
            Image(systemName: "plus")
                .font(.system(.largeTitle, design: .rounded, weight: .medium))
                .foregroundStyle(Storybook.forest.opacity(0.5))
                .position(x: width / 2, y: height / 2)
                .accessibilityHidden(true)
        }
    }

    private func sourceCenter(width: CGFloat, height: CGFloat) -> CGPoint {
        compact ? CGPoint(x: width / 2, y: 130) : CGPoint(x: width * 0.27, y: height / 2)
    }

    private func destinationCenter(width: CGFloat, height: CGFloat) -> CGPoint {
        compact ? CGPoint(x: width / 2, y: 407) : CGPoint(x: width * 0.79, y: height / 2)
    }

    private func position(for id: Int, width: CGFloat, height: CGFloat) -> CGPoint {
        if round.kind == .addition {
            if round.isJoined {
                return gridPoint(index: id, count: round.total, center: CGPoint(x: width / 2, y: height / 2), spacing: 90)
            }
            let isLeft = id < round.addLeft
            return gridPoint(index: isLeft ? id : id - round.addLeft, count: isLeft ? round.addLeft : round.addRight, center: isLeft ? sourceCenter(width: width, height: height) : destinationCenter(width: width, height: height), spacing: 88)
        }
        if round.selected.contains(id) {
            let packedIndex = round.selected.sorted().firstIndex(of: id) ?? 0
            var center = destinationCenter(width: width, height: height)
            if round.kind == .counting { center.y -= 27 }
            return gridPoint(index: packedIndex, count: round.selected.count, center: center, spacing: 84)
        }
        // Unmoved berries retain their original spaces so removing one never shifts another under a finger.
        return gridPoint(index: id, count: round.total, center: sourceCenter(width: width, height: height), spacing: 88)
    }

    private func gridPoint(index: Int, count: Int, center: CGPoint, spacing: CGFloat) -> CGPoint {
        let columns = min(3, max(1, count))
        let rows = max(1, (count + columns - 1) / columns)
        return CGPoint(x: center.x + (CGFloat(index % columns) - CGFloat(columns - 1) / 2) * spacing,
                       y: center.y - 10 + (CGFloat(index / columns) - CGFloat(rows - 1) / 2) * 86)
    }
}

private struct MathPieceButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
    }
}
