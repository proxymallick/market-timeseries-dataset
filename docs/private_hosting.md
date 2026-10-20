# Authorized private hosting

On 2026-10-10 Sydney, I authorized a private GitHub repository and a restricted Google Drive folder for review copies. This does not authorize public release, wider sharing, or distribution of unresolved sources.

- Private repository: https://github.com/proxymallick/market-timeseries-dataset
- Private dataset folder: https://drive.google.com/drive/folders/1hK1fNAr8fH_LyNXnXjuVHhQqMOBDm8vq
- The six dataset ZIPs contain the 54 hash-pinned payloads, schemas, dataset card, terms, and attribution. `hosting/drive_archive_manifest.json` records their sizes and hashes.
- The Drive folder contains the original ten-file review package: six dataset archives, the documentation ZIP, paper PDF, index JSON, and README.
- The private `data_restricted/` backup contains 32,654 files and 237,170,229,566 bytes (237.17 GB, or 220.88 GiB). I started the upload on 2026-10-17, retried failed transfers, and Drive reported it complete on 2026-10-20. This is a private preservation copy of held source material, not the 106.9 MB reviewed release candidate or a public download.
- These are review copies, not a public data release or a new license. The paper has no registered DOI.

The existing CLI token could not create or write the repository, and SSH had no usable key. I created it through the signed-in browser and pushed `prepare-release` with GitHub Desktop. Local and remote tracking matched commit `7a44d628e2cedee058d69c440d8cb5ceb96eecd2` after the first push. No credential value was read or copied into the project.

Public-host metrics remain unconfigured. Keyless APIs cannot read private traffic, and I use Drive only for review storage, not as a download counter or DOI host.

## Final storage verification

Drive confirmed that all ten prepared-package files are in the named folder. The share dialog lists only me and shows General access as Restricted. I checked the six dataset archives against all 54 manifest paths and verified their hashes and ZIP integrity before upload. I did not download the remote files again for a round-trip hash check. The documentation ZIP preserves commit `7a44d62`; GitHub contains later status updates.

The full `data_restricted/` upload is separate from the prepared-package verification. At completion, Drive showed `data_restricted` in the restricted folder, reported “1 upload complete,” and showed 36,684 of 36,684 upload entries at 100%. The entry count includes folders as well as the 32,654 files. Drive showed 276.66 GB of 400 GB account storage used. I did not change the folder's restricted access setting.
