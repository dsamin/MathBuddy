# Local Git baseline — October 3, 2026

The user authorized preservation of meaningful work and a local Git checkpoint. No repository URL was supplied; no remote or GitHub repository was created and no push was attempted.

A focused read-only audit reviewed native source/project configuration, scripts, documentation/catalogs, browser studies, and image/audio metadata. Initial inventory: 199 meaningful files totaling 24,694,488 bytes, including two build logs excluded from the checkpoint. Largest binary: 2,632,805 bytes. Ordinary Git is appropriate for these small candidate assets; no LFS configuration is required at this size.

The broad `output/` ignore was replaced with specific build-log exclusions to retain authored fixtures and the earlier planning snapshot. Build/caches, local environment/secret stores, signing credentials and machine-specific Xcode files remain excluded. CSV line endings were normalized from CRLF to LF without changing catalog records to resolve Git whitespace warnings.

The reviewer decoded 21 PNG/JPG outputs, parsed all JSON and measured the 19 original narration masters (24 kHz, mono PCM16, nonempty). Existing hashes/bundled copies matched. These are technical preservation checks only. All existing native work, illustrations, recordings and mockups remain unapproved experiments at their original locations.

Staged changes were inspected by file/category and size. `gitleaks git --staged --redact --no-banner` reported no leaks; the final precommit whitespace and secret checks are required again after this record is staged. No generated attribution or contributor trailer is permitted.

The requested `~/.Codex/IDEAS.md` was absent; no replacement notebook was created.
