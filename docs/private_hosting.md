# Authorized private hosting

On 2026-10-10 Sydney, I authorized a private GitHub repository and a restricted Google Drive folder for review copies. This does not authorize public release, wider sharing, or distribution of unresolved sources.

- Private repository: https://github.com/proxymallick/market-timeseries-dataset
- Private dataset folder: https://drive.google.com/drive/folders/1hK1fNAr8fH_LyNXnXjuVHhQqMOBDm8vq
- The six dataset ZIPs contain the 54 hash-pinned payloads, schemas, dataset card, terms, and attribution. `hosting/drive_archive_manifest.json` records their sizes and hashes.
- The Drive folder contains ten files: six dataset archives, the documentation ZIP, paper PDF, index JSON, and README. Only the prepared selection and its documentation were uploaded; the 237 GB of held inputs remain local.
- These are review copies, not a public data release or a new license. The paper has no registered DOI.

The existing CLI token could not create or write the repository, and SSH had no usable key. I created it through the signed-in browser and pushed `prepare-release` with GitHub Desktop. Local and remote tracking matched commit `7a44d628e2cedee058d69c440d8cb5ceb96eecd2` after the first push. No credential value was read or copied into the project.

Public-host metrics remain unconfigured. Keyless APIs cannot read private traffic, and I use Drive only for review storage, not as a download counter or DOI host.

## Final storage verification

Drive confirmed that all ten files are in the named folder. The share dialog lists only me and shows General access as Restricted. I checked the six dataset archives against all 54 manifest paths and verified their hashes and ZIP integrity before upload. I did not download the remote files again for a round-trip hash check. The documentation ZIP preserves commit `7a44d62`; GitHub contains later status updates.
