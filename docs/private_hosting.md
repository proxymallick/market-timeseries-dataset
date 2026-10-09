# Authorized private hosting

On 2026-10-10 Sydney the owner authorized a private GitHub repository and use of their Google Drive for appropriate datasets. This updates the earlier local-only boundary for these private destinations. Public release, wider sharing and unresolved-source distribution remain unapproved.

- Private repository: https://github.com/proxymallick/market-timeseries-dataset
- Private dataset folder: https://drive.google.com/drive/folders/1hK1fNAr8fH_LyNXnXjuVHhQqMOBDm8vq
- Six dataset ZIP files retain the 54 hash-pinned payloads, source-specific schemas, dataset card, source terms and attribution. The CFTC companion remains another representation of the same rows. `hosting/drive_archive_manifest.json` records archive sizes and hashes.
- Google Drive reported all ten uploads complete: six dataset archives, project-documentation ZIP, dataset paper PDF, index JSON and README. Uploads used the native macOS file picker after extension-assisted upload was unavailable. The Drive folder receives only the prepared conditional selection and documentation. The 237 GB of held inputs remain local.
- These are private review copies, not an open-source data publication or a new blanket license. The paper describes the dated preparation snapshot and has no registered DOI.

The existing CLI token cannot create or write the new repository, and SSH has no usable authentication. Repository creation succeeded through the owner's signed-in browser. GitHub Desktop subsequently authenticated successfully and pushed branch `prepare-release`. The local and remote tracking commit matched `7a44d628e2cedee058d69c440d8cb5ceb96eecd2` after the push; no CLI token expansion was needed. No credential values were read or copied into the project.

Public metrics configuration remains empty. Keyless APIs cannot provide private-repository counters. Google Drive is storage for the private review copies; it is not presented as a persistent download-counter or DOI host.

## Final storage verification

Google Drive confirmed all ten files were moved from My Drive into the named dataset folder. The folder share dialog lists only the owner and General access: Restricted. The six dataset archives contain all 54 manifest-listed payloads; archive hashes and ZIP integrity were verified locally before upload. Remote file bytes were not downloaded again for a round-trip hash check. The documentation ZIP is the immutable `7a44d62` preparation snapshot; GitHub contains subsequent private-hosting status updates.
