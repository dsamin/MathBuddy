import AVFoundation
import Observation

/// Plays files bundled with the app. No speech synthesis or network provider runs on iPad.
@MainActor
@Observable
final class MathBuddyAudio {
    private(set) var playbackNotice: String?
    @ObservationIgnored private var narration: AVAudioPlayer?
    @ObservationIgnored private var effect: AVAudioPlayer?

    var availableNarration: Bool { resource("welcome") != nil }

    func playNarration(_ key: String, enabled: Bool) {
        narration?.stop()
        guard enabled else { return }
        guard let url = resource(key) else {
            playbackNotice = "This spoken prompt is unavailable. You can keep playing with the pictures."
            return
        }
        do {
            try configureAudio()
            narration = try AVAudioPlayer(contentsOf: url)
            narration?.volume = 0.85
            narration?.prepareToPlay()
            narration?.play()
            playbackNotice = nil
        } catch {
            playbackNotice = "Sound is unavailable right now. The activity still works."
        }
    }

    func playEffect(_ key: String, enabled: Bool) {
        effect?.stop()
        guard enabled, let url = resource("effect-" + key) else { return }
        do {
            try configureAudio()
            effect = try AVAudioPlayer(contentsOf: url)
            effect?.volume = 0.28
            effect?.play()
        } catch {
            playbackNotice = "Sound effects are unavailable right now."
        }
    }

    func stop() {
        narration?.stop()
        effect?.stop()
    }

    private func configureAudio() throws {
        try AVAudioSession.sharedInstance().setCategory(.ambient, mode: .default)
        try AVAudioSession.sharedInstance().setActive(true)
    }

    private func resource(_ name: String) -> URL? {
        Bundle.main.url(forResource: name, withExtension: "wav", subdirectory: "Audio")
            ?? Bundle.main.url(forResource: name, withExtension: "wav")
    }
}
