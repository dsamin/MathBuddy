# Lessons

## 2026-10-03 — Native platform is not permission to implement

- The user wanted an overall feature spec, then individually reviewed assets, then individual phase plans, aligned with Pebble. Building the native app during that planning request exceeded scope.
- “Proper iPad app” and “not a JavaScript web page” constrain the eventual platform. They do not by themselves authorize an Xcode project, implementation, builds, generated production assets, or provider spending during a spec/mockup task.
- Preserve the requested stage: specification → asset direction → reviewed asset batches → plan one build phase → execute that phase when requested. Do not collapse this sequence because tools are available.
- Treat existing premature code/art/audio as unapproved experiments. A successful build or file-quality check is neither product approval nor approval to keep the design.
- For planning requests, deliver concrete documents and reviewable choices. Do not turn them into implementation work.

## Earlier interpretation — superseded

The earlier rule to generate and run an Xcode target whenever the user says native iPad was too broad. Native architecture and iPad-specific mockups can be specified without building an app. Preserve explicit asset provenance and honest testing limits, but do not use them to justify work outside the requested stage.
