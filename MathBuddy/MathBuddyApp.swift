import SwiftUI
import AVFoundation

@main
struct MathBuddyApp: App {
    @State private var store = MathBuddyStore()
    @State private var audio = MathBuddyAudio()
    @Environment(\.scenePhase) private var scenePhase

    var body: some Scene {
        WindowGroup {
            MathBuddyRootView(store: store, audio: audio)
                .onReceive(NotificationCenter.default.publisher(for: AVAudioSession.interruptionNotification)) { _ in
                    audio.stop()
                }
                .onChange(of: scenePhase) {
                    if scenePhase != .active {
                        audio.stop()
                        store.save()
                    }
                }
        }
    }
}
