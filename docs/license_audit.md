# Licensing audit — local preparation

Accessed 2026-10-09 UTC. This is a technical rights review, not legal advice. Official dataset grants, API/service terms and venue policies were checked separately. Current venue policy does not conclusively establish historical contractual applicability; unresolved cases are excluded rather than asserted illegal.

Every inventoried physical file is mapped in the private per-file CSV. Decisions are source-family classifications; they do not automatically clear every artifact. Release eligibility requires a separate conditions check. Original data are not moved.

| Source family | Status | Applicable license/terms | Affected files* |
|---|---|---|---:|
| CFTC Commitments of Traders (COT), including Traders in Financial Futures (TFF) | ⚠️ Redistribute with conditions | CFTC website public-domain statement; no SPDX license assigned | 9 |
| Daily Treasury par-yield curve rates | ❓ Unclear | UNVERIFIED | 38 |
| USDA WASDE reports and NAL ESMIS archive (including associated release files) | ⚠️ Redistribute with conditions | NAL website public-domain/copyright guidance; no SPDX license assigned | 73 |
| Federal Reserve Board economic release documents | ⚠️ Redistribute with conditions | Federal Reserve Board website public-domain statement; no SPDX license assigned | 1256 |
| FDIC Failed Bank List / failed-bank data | ❓ Unclear | UNVERIFIED | 5 |
| ABS macro statistical releases (CPI, PPI, Labour Force, GDP/national accounts, retail, WPI, building approvals, trade) | ⚠️ Redistribute with conditions | CC BY 4.0 for general ABS website material, subject to exceptions and release-specific notices | 1700 |
| RBA monetary-policy and selected financial-system media release events | ⚠️ Redistribute with conditions | CC BY 4.0 for ordinary RBA material, subject to third-party and other excluded-material terms | 271 |
| RBA Statistical Table F2 daily government bond yields (local 2013–2025 dataset) | ⚠️ Redistribute with conditions | RBA Financial Data terms, Copyright and Disclaimer Notice section 5; separate from general CC BY 4.0 grant | 2 |
| AOFM issuance program, forthcoming tender schedule and transaction/result documents | ⚠️ Redistribute with conditions | CC BY 4.0 for AOFM-produced website material, subject to exceptions | 8 |
| FI-2010 | ❓ Unclear | Creative Commons Attribution 4.0 International | 109 |
| Hyperliquid Open Book: Level 4 Order Book Data (Zenodo record 18184441) | ⚠️ Redistribute with conditions | Creative Commons Attribution 4.0 International | 12 |
| Hyperliquid Open Book derived hourly OHLC | ⚠️ Redistribute with conditions | CC BY 4.0 conditions inherited from source material; no separate upstream license for this project's derived files identified | 3 |
| High Frequency Crypto Limit Order Book Data (Kaggle martinsn/high-frequency-crypto-limit-order-book-data) | ❓ Unclear | CC0: Public Domain (Kaggle dataset metadata); Coinbase source-data terms may separately apply | 10 |
| Yahoo Finance continuous futures exports and all derived market panels | ❌ Do not redistribute | Yahoo Terms of Service; data are not licensed by yfinance's Apache-2.0 code license | 50 |
| Binance Vision spot klines and derived hourly/selection tables | ⚠️ Redistribute with conditions | CC BY-NC-SA 4.0 plus Binance Vision Dataset Terms version 1.0 (2026-08-26) | 98 |
| FinCast-Paper-test and all derived daily/PCIE/zero-shot tables | ❓ Unclear | Publisher labels repository Apache-2.0; underlying market-data rights chain UNVERIFIED | 1998 |
| Qlib Chinese-equity provider feature binaries and archive | ❓ Unclear | UNVERIFIED | 27131 |
| Unidentified market fixtures, microstructure sample and model/analysis artifacts | ❓ Unclear | UNVERIFIED | 23903 |

* A multi-source file may appear in more than one family. Counts are physical files, not independent datasets.

## Evidence and obligations

### cftc: U.S. Commodity Futures Trading Commission (CFTC)

The CFTC terms page expressly says government information made available on its website is public domain and may be freely distributed and copied, requests acknowledgment, and excepts third-party contributed/licensed material. Official TFF data portal page was fetched successfully. This policy is broad agency-site guidance, not an artifact-level statement for every archive file.

- Redistribution: CFTC states government information on its website may be freely distributed and copied. This covers agency-created COT/TFF material to the extent the particular file contains no third-party protected material.
- Commercial use: No noncommercial-only restriction appears in the CFTC statement; commercial redistribution of CFTC-created public-domain information is therefore supported, subject to third-party material exceptions.
- Attribution: CFTC requests appropriate acknowledgment in subsequent use.
- Share-alike: No share-alike condition stated.
- Derived data: No special COT/TFF derived-data rule located. The cited CFTC policy provides no share-alike or downstream licensing requirement for agency-created content; do not include protected third-party material without permission.
- Restrictions: CFTC says contributed or licensed third-party documents, illustrations, photographs, and other resources may be copyrighted and require permission beyond fair use. Do not use CFTC seals/logos to imply endorsement; verify exact artifacts for third-party notices.
- Verification: verified_official_policy_and_source_page; accessed 2026-10-09T12:36:48Z
- Official sources: [source 1](https://accountcreation.cftc.gov/TermsOfUseAgreement.aspx)
- Alternative: Use only the numeric COT/TFF tables and agency explanatory text, preserve CFTC source attribution, omit artwork/seals and any separately credited content, and retain the exact source file and its notices.

### treasury: U.S. Department of the Treasury

Official page supplies daily rates, downloadable CSV and XML; official feed documentation gives endpoints and historical availability. Neither page states a copyright/license or commercial redistribution permission. Public-domain status is not assumed.

- Redistribution: Official daily rates page and XML feed document the downloadable/GET data, but the reviewed pages do not state reuse or redistribution rights. No dataset-specific license or explicit public-domain reuse policy was verified.
- Commercial use: Unclear from the official daily-rate and XML feed pages reviewed; commercial redistribution rights are not established by data availability alone.
- Attribution: No dataset-specific attribution requirement or recommendation located on the reviewed rate/feed pages.
- Share-alike: No share-alike term located.
- Derived data: No derived-data permissions or restrictions located in the reviewed data/feed documentation; no license conclusion should be inferred for commercial derived products.
- Restrictions: The Treasury site can host third-party content, as shown by unrelated materials with their own copyright legends; rights must be checked on any material included in a release. No explicit seals/logo guidance was verified for this dataset.
- Verification: official_data_pages_verified_terms_not_found; accessed 2026-10-09T12:36:48Z
- Official sources: [source 1](https://home.treasury.gov/treasury-daily-interest-rate-xml-feed)
- Alternative: Seek written confirmation from Treasury for redistribution rights, or exclude the raw rate series and provide only independently calculated outputs after counsel confirms the legal basis.

### usda: World Agricultural Outlook Board / National Agricultural Library, U.S. Department of Agriculture

ESMIS identifies WASDE as prepared/released by WAOB and provides monthly reports in multiple formats. NAL's policy allows free copying/distribution for most NAL information but explicitly excepts certain protected material. The policy is general to NAL and does not establish an unconditional license for all report inclusions.

- Redistribution: NAL says most information on its website is public domain and freely distributed or copied. That statement is qualified: some material is copyright-, trademark-, or patent-restricted, or personal-use-only, and linked-site terms apply.
- Commercial use: For agency-created WASDE content, the NAL wording allows free distribution/copying without a noncommercial limit, supporting commercial reuse subject to identifying and clearing embedded third-party material.
- Attribution: NAL requests the credit: National Agricultural Library, Agricultural Research Service, U.S. Department of Agriculture. For WASDE-specific use, identify USDA/World Agricultural Outlook Board and cite the report/version.
- Share-alike: No share-alike condition stated in the NAL policy.
- Derived data: No general derived-data rule located. No share-alike requirement appears in the cited policy; underlying incorporated third-party material remains subject to its own terms.
- Restrictions: NAL cautions that some site materials have third-party copyright/trademark/patent or personal-use restrictions and requires users to check linked content. ESMIS lists PDF, TXT, XLS, and XML release artifacts; check each report and supplemental file for notices before redistributing complete files. Avoid USDA seals/logos or endorsement implications absent permission.
- Verification: verified_official_policy_and_archive_page_artifact_level_not_fully_verified; accessed 2026-10-09T12:36:48Z
- Official sources: [source 1](https://www.nal.usda.gov/web-policies-and-important-links)
- Alternative: Redistribute extracted USDA-authored numerical tables with attribution after checking report-level notices; exclude report graphics or material credited to outside sources, or obtain permissions for complete-document redistribution.

### fed: Board of Governors of the Federal Reserve System

Federal Reserve disclaimer expressly permits copying/distribution of Board website information unless otherwise indicated, requests source citation, and specifies third-party content and seal/logo restrictions. The official release archive is the target source family; check individual releases for labeled exceptions.

- Redistribution: Unless otherwise indicated, the Board says website information is public domain and may be copied and distributed without permission. This applies to Board-originated release content subject to identified non-Board material exceptions.
- Commercial use: The policy has no noncommercial restriction for Board-originated public-domain content; commercial copying/distribution is supported subject to non-Board material rights.
- Attribution: Board requests citation to the Board as the source.
- Share-alike: No share-alike condition stated.
- Derived data: No general derived-data or share-alike condition stated for Board-originated website information.
- Restrictions: Photos, graphics, or other material identified as associated with a non-Board source require permission from that source. Board seals, logos, and official insignia are protected and may not be used or reproduced without written permission; federal law also limits misleading use of Federal Reserve words/symbols. External linked content retains its own rights.
- Verification: verified_official_policy_and_release_index; accessed 2026-10-09T12:36:48Z
- Official sources: [source 1](https://www.federalreserve.gov/disclaimer.htm)
- Alternative: Use Board-authored release text and tables with attribution; exclude externally credited imagery, third-party attachments and Board insignia.

### fdic: Federal Deposit Insurance Corporation (FDIC)

FDIC page confirms the list includes banks failed since October 1, 2000 and offers Download Data. A 403 prevented direct public GET of the FDIC Archive copyright page in this collection attempt, although the official page was accessible through search results and states Archive information created by/for government is public domain, freely copied/distributed with acknowledgment. That archive-specific policy does not resolve the separate Failed Bank List data rights.

- Redistribution: The official failed-bank list page offers a download, but the reviewed page contains no dataset-specific copyright or redistribution terms. FDIC Archive copyright guidance applies to the FDIC Archive and its documents; it does not clearly say it governs this separate failed-bank listing/data download.
- Commercial use: Unclear for the Failed Bank List download; commercial reuse is not established by the listing/download page reviewed.
- Attribution: The Archive policy requests FDIC acknowledgment for public-domain Archive materials, but applicability to this distinct dataset is unverified. Attribute FDIC provisionally if using while seeking clarification.
- Share-alike: No share-alike term located for the failed-bank list.
- Derived data: No failed-bank-list derived-data terms located.
- Restrictions: Do not extrapolate the FDIC Archive policy to other FDIC products without confirmation. Review any downloaded file for embedded notices and third-party material. No dataset-specific seal/logo guidance verified.
- Verification: official_data_page_verified_related_policy_scope_unconfirmed; accessed 2026-10-09T12:36:48Z
- Official sources: [source 1](https://archive.fdic.gov/Content%20and%20Copyright)
- Alternative: Ask FDIC to confirm reuse terms for the downloadable Failed Bank List. Until then, avoid redistributing the raw dataset; use independently derived facts only after rights review.

### abs: Australian Bureau of Statistics, Commonwealth of Australia

ABS website terms say ABS-produced website material is CC BY 4.0 except Coat of Arms, logo, trademarks, microdata, third-party content and specified brands/artwork; third-party copyright remains with owner. Conditions of Sale state most ABS material is CC BY, but where no license is indicated full copyright terms apply. CC BY allows copying, derivatives and commercial use with attribution and license disclosure.

- Redistribution: Allowed for ABS-created CC BY material with attribution and license notice; third-party content, microdata, logos/marks and named excluded brands/artwork are outside the grant and may require permission. Verify each release/product notice.
- Commercial use: Allowed for covered CC BY 4.0 content. Product with no stated license may be under full copyright terms; ABS Conditions of Sale restrict reproduction/commercialization except as licensed.
- Attribution: Unchanged: 'Source: Australian Bureau of Statistics' or 'Source: ABS'. Modified/derived: 'Based on Australian Bureau of Statistics data' or 'Based on ABS data'. Do not imply endorsement.
- Share-alike: No share-alike condition under CC BY 4.0.
- Derived data: Adaptation/derivatives permitted for covered material with attribution and clear license terms; don't attribute transformations to ABS as its own. Check product-specific and third-party terms.
- Restrictions: ["Coat of Arms, ABS logo, trademarks, microdata, third-party content and specified sub-brands/artwork are excluded.", "Release/product notice controls; no license indication may mean full copyright terms.", "No implied ABS/Commonwealth endorsement."]
- Verification: verified_current_official_terms; per-release product notices still require review; accessed 2026-10-09T12:38:02Z
- Official sources: [source 1](https://www.abs.gov.au/website-privacy-copyright-and-disclaimer), [source 2](https://www.abs.gov.au/about/legislation-and-policy/purchasing-data/abs-conditions-sale), [source 3](https://creativecommons.org/licenses/by/4.0/legalcode)
- Alternative: Use only explicitly CC BY 4.0 ABS release material after checking embedded third-party content; otherwise link to official release or obtain permission.

### rba_events: Reserve Bank of Australia

RBA notice grants CC BY 4.0 to most material, excluding third-party material and specified categories. It requires attribution in a stated format. economic_events/sources.md records RBA media releases as date-only because index/page date does not prove release instant.

- Redistribution: Allowed for ordinary RBA-authored release material with attribution; material containing/derived from/using third-party content needs third-party consent or its own published license. Review each release page.
- Commercial use: Allowed for CC BY-covered material with attribution and no implied RBA endorsement. Special Cash Rate/Financial Data terms apply if numerical series/material is included.
- Attribution: Unless specified otherwise: 'Source: Reserve Bank of Australia [year]' or 'Source: RBA [year]'. Do not imply endorsement.
- Share-alike: No share-alike condition under CC BY 4.0.
- Derived data: Adapt CC BY-covered RBA text with attribution. Third-party material requires its own consent/license; preserve source URL/provenance. Event title/date rows in local inventory are date-only pending verified publication timestamps.
- Restrictions: ["Third-party material excluded and may require permission.", "Logo, banknotes, Cash Rate, Financial Data, multimedia and site infrastructure have separate terms.", "No unlawful use or implied RBA endorsement."]
- Verification: verified_current_official_terms; individual release sources require review; accessed 2026-10-09T12:38:02Z
- Official sources: [source 1](https://www.rba.gov.au/copyright/), [source 2](https://creativecommons.org/licenses/by/4.0/legalcode), [source 3](https://www.rba.gov.au/media-releases/2026/)
- Alternative: Keep only source-linked event metadata after reviewing each release for third-party labels; otherwise link to official pages without republishing their content.

### rba_f2: Reserve Bank of Australia; current official F2 CSV metadata lists Source=RBA for each of five series

RBA section 5 separately governs Financial Data and permits commercial use subject to attribution/non-endorsement and other terms; it expressly requires third-party permission/license for third-party-derived/prepared data. The downloaded official F2 CSV describes daily interpolated AGS yields and lists Source=RBA for each series. RBA change notice says AGS F2 series were replaced by yields assessed by RBA, informed by market participants but using RBA judgment. Local manifest names Financial Data terms and the third-party caveat.

- Redistribution: Personal and commercial reproduction/publication/public communication allowed under section 5 conditions. Do not misrepresent source, imply RBA endorsement, or charge access without telling users RBA publishes it free. Any third-party-derived/prepared data needs third-party consent/license. F2 Source=RBA supports RBA attribution; review provenance before bulk mirroring.
- Commercial use: Permitted subject to section 5: attribution, non-endorsement, no unlawful use or improper exploitation; fee for access must disclose the free RBA publication. RBA does not administer F2 as a benchmark.
- Attribution: 'Source: Reserve Bank of Australia [year]' or 'Source: RBA [year]' unless the material specifies otherwise. Current CSV Source row lists RBA for all series.
- Share-alike: No share-alike stated; do not infer a CC/SPDX license for this Financial Data category.
- Derived data: Derived/use-reference is allowed under section 5 conditions; avoid implied RBA endorsement or improper commercial exploitation. Third-party inputs retain their own terms. RBA may change methodology, availability or schedule without notice.
- Restrictions: ["Not administered as a financial benchmark; RBA does not recommend it as one.", "No implied RBA endorsement; no unlawful use or improper commercial exploitation.", "Third-party content in, derived from or used to prepare a financial series requires permission/license.", "RBA may alter, revise or withdraw data; disclaimers apply."]
- Verification: verified_current_official_terms_and_live_CSV_XLSX; local manifest/hash inspected; preserve third-party exception caveat; accessed 2026-10-09T12:38:02Z
- Official sources: [source 1](https://www.rba.gov.au/copyright/), [source 2](https://www.rba.gov.au/statistics/tables/), [source 3](https://www.rba.gov.au/statistics/tables/changes-to-tables.html), [source 4](https://www.rba.gov.au/statistics/tables/csv/f2-data.csv), [source 5](https://www.rba.gov.au/statistics/tables/xls/f02d.xlsx)
- Alternative: If bulk redistribution provenance cannot be confirmed, publish derived features with RBA attribution and link to F2; AOFM CC BY auction result data is an event-level alternative, not a constant-maturity yield substitute.

### aofm: Australian Office of Financial Management, Commonwealth of Australia

AOFM copyright page says website material is CC BY 4.0 except Coat of Arms, AOFM logo, trademarks and third-party material; attribution is agency name without endorsement. Current forthcoming schedule lists proposed next-week tender terms; program page says details of weekly offerings announced Friday at midday. Those are schedule announcements, not necessarily the publication times for results.

- Redistribution: Permitted for AOFM-produced content with attribution and no implied endorsement; third-party material, marks/logo and Coat of Arms excluded. Check each document/workbook for notices.
- Commercial use: Permitted for CC BY-covered material; third-party elements remain subject to owner terms.
- Attribution: 'Australian Office of Financial Management'; do not imply Commonwealth endorsement.
- Share-alike: No share-alike condition under CC BY 4.0.
- Derived data: CC BY permits adaptations and derivatives with attribution/license notice. Preserve AOFM provenance; inspect third-party information in syndication and transaction documents. Schedule pages report planned transactions; do not infer an unshown release timestamp.
- Restrictions: ["Coat of Arms, AOFM logo, trademarks and third-party content excluded.", "Third-party copyright remains with owner; permission may be required.", "Planned weekly schedule/result timings are mutable."]
- Verification: verified_current_official_terms_and_schedule; individual historical documents need notice review; accessed 2026-10-09T12:38:02Z
- Official sources: [source 1](https://www.aofm.gov.au/copyright), [source 2](https://www.aofm.gov.au/program), [source 3](https://www.aofm.gov.au/program/issuance-program), [source 4](https://www.aofm.gov.au/data-hub), [source 5](https://creativecommons.org/licenses/by/4.0/legalcode)
- Alternative: Use AOFM Data Hub result workbooks/schedule pages with attribution after checking each notice and excluding third-party material; keep date-only status unless source supplies exact publication instant.

### fi2010: Fairdata / Tampere University of Technology dataset record; creators Adamantios Ntakaris, Martin Magris, Juho Kanniainen et al.; venue data from Nasdaq Helsinki

The live Fairdata API provides the record's CC BY 4.0 label and open access status. The current official September 2026 Nasdaq European Data Policies describe internal-use limits for subscriber-sourced Nordic/Baltic historical data exceeding five depth levels. Fairdata's grant is clear at the publication layer, while the underlying rights chain is not.

- Redistribution: The live Fairdata record explicitly labels the published normalized benchmark open and CC BY 4.0, which permits commercial redistribution with attribution. However this is a 10-level MBP benchmark sourced from Nasdaq Helsinki; Nasdaq's current September 2026 European Data Policies restrict redistribution of Nordic/Baltic historical data with over five levels to internal use absent an applicable redistribution entitlement. The benchmark authors' authority to grant CC BY rights in this transformed corpus, and whether all relevant exchange rights are cleared, are not established by the dataset record alone. Resolve the source entitlement or limit release to independently created summaries before distributing raw/near-raw files commercially.
- Commercial use: CC BY 4.0 permits commercial use subject to attribution; upstream Nasdaq market-data rights and the authors' sublicensing authority remain unresolved for commercial redistribution of the 10-level records.
- Attribution: Attribute the dataset creators (Ntakaris, Magris, Kanniainen et al.), link the Fairdata record and CC BY 4.0, identify modifications, and retain notices.
- Share-alike: No share-alike obligation under CC BY 4.0.
- Derived data: CC BY 4.0 allows adaptations and commercial reuse with attribution and indication of changes; it does not impose share-alike. Because the supplied benchmark contains 10 depth levels and Nasdaq policy for subscriber-sourced historical data restricts onward redistribution over five levels, the rights chain for direct or lightly transformed extracts should be clarified before release. Aggregate research findings may have lower data-retention risk, but this is not a rights determination.
- Restrictions: ["Fairdata metadata is explicit CC BY 4.0, but is not proof that the uploaders cleared the source exchange's rights.", "Nasdaq European Data Policies (September 2026) states subscriber use of Nordic/Baltic historical data with more than five levels is internal-use only and may not be forwarded to third parties; applicability to this publisher-authorized historical benchmark is uncertain.", "Do not use the local README's 'safe/openly licensed' characterization as the basis for release; the live Fairdata record and the venue-policy caveat control this audit."]
- Verification: live Fairdata API verified (HTTP 200); current September 2026 official Nasdaq policy PDF captured; applicability of venue subscriber policy and source clearance unresolved; accessed 2026-10-09T12:38:12Z
- Official sources: [source 1](https://creativecommons.org/licenses/by/4.0/), [source 2](https://www.nasdaq.com/docs/data/Nasdaq_European_Data_Policies_September_2026), [source 3](https://www.nasdaq.com/products/data/european-pricing-policies)
- Alternative: For a clearly redistributable equity LOB corpus, use a dataset with a documented rights chain that expressly clears the original venue feed, or obtain written permission/licensing from Nasdaq and/or the dataset authors for commercial redistribution.

### hyperliquid: Zenodo record by Jakob Albers, Mihai Cucuringu, Sam Howison, and Alexander Y. Shestopaloff; data describes the Hyperliquid L1

The retained record metadata identifies CC BY 4.0 and the four dataset creators. Hyperliquid's official support guide identifies its official site and documentation. The corpus contains user/address identifiers; that creates privacy and linkability considerations, but no venue-specific redistribution ban was confirmed. Primary-agent follow-up captured current DataCite DOI metadata, which confirms the publisher-registered CC-BY-4.0 grant. Zenodo record UI/API availability remains unverified.

- Redistribution: CC BY 4.0 allows redistribution, including commercially, provided attribution, license link, and change notices are supplied. The dataset is account-linked and includes wallet/user identifiers and order/trade activity; address linkage and participant re-identification should be assessed before publishing detailed records or derived tables. No venue prohibition on dataset redistribution was verified, and none is asserted here.
- Commercial use: Allowed by CC BY 4.0 with attribution and other license conditions; separately assess privacy, data-protection, and participant-linkability concerns.
- Attribution: Cite Albers, Cucuringu, Howison, and Shestopaloff (2026), the Zenodo record DOI 10.5281/zenodo.18184441, and CC BY 4.0; identify changes and keep the license link.
- Share-alike: No share-alike obligation under CC BY 4.0.
- Derived data: Redistribute adapted or extracted material under CC BY 4.0 attribution conditions and mark modifications. Dataset-specific license metadata is in the previously retained Zenodo record snapshot; the live Zenodo API returned HTTP 403 and its record HTML timed out during this audit, so the current record was not independently refreshed. Minimize wallet identifiers in public outputs where they are unnecessary.
- Restrictions: ["Zenodo live API request returned HTTP 403 and the HTML record timed out; current license metadata was corroborated from an existing local Zenodo API record snapshot, not live-verified in this audit.", "Wallet/user identifiers are public pseudonymous data but can support linkage and sensitive behavioural inference; conduct privacy and re-identification review for detailed releases.", "Hyper Foundation service terms were located, but the captured route returned a JavaScript shell and did not establish a prohibition on reuse of the on-chain dataset. Do not infer a venue ban from the terms without evidence."]
- Verification: license corroborated from retained Zenodo record snapshot; fresh Zenodo API fetch failed (403) and record HTML timed out; venue terms page shell captured but not independently parsed; fresh authoritative DOI registry HTTP 200 confirms CC-BY-4.0, creators and title; accessed 2026-10-09T12:42:45Z
- Official sources: [source 1](https://creativecommons.org/licenses/by/4.0/), [source 2](https://hyperfoundation.org/), [source 3](https://www.hyperfoundation.us/termsOfService), [source 4](https://hyperliquid.gitbook.io/hyperliquid-docs/support), [source 5](https://api.datacite.org/dois/10.5281/zenodo.18184441)
- Alternative: Publish address-free aggregate statistics or a limited OHLC feature set with source attribution; for raw wallet/order lifecycle data, obtain a fresh official Zenodo record response and complete privacy/legal review before public release.

### hyperliquid_hourly: Derived by this project from the Hyperliquid Open Book trade stream (Zenodo record 18184441)

The source record snapshot states CC BY 4.0. Hourly OHLC drops account identifiers when built from trade timestamps, prices, and sizes, but attribution and change notices remain appropriate for a derived redistribution. Primary-agent follow-up captured current DataCite DOI metadata, which confirms the publisher-registered CC-BY-4.0 grant. Zenodo record UI/API availability remains unverified.

- Redistribution: Hourly OHLC generated from the CC BY 4.0 trade stream can be shared commercially with source attribution, license link, and a notice that the data were aggregated/modified. The OHLC is address-free if generated solely from timestamps, prices, and sizes; confirm no wallet IDs or source JSON rows are embedded in companion files. No Hyperliquid venue prohibition on OHLC reuse was verified.
- Commercial use: Allowed under CC BY 4.0 with attribution and change notices, subject to source-license verification and privacy review if identifiers are retained.
- Attribution: Cite Albers et al. (2026), DOI 10.5281/zenodo.18184441, and CC BY 4.0; label the output as derived hourly OHLC and describe the aggregation/modifications.
- Share-alike: No share-alike obligation under CC BY 4.0.
- Derived data: The hourly OHLC is an adaptation/aggregation of the source trades. Keep attribution, license URL, and modification notice. Do not include wallet/user identifiers unless separately justified and reviewed. The upstream Zenodo record could not be refreshed live during this audit (API 403; HTML timeout), so reconfirm its current license metadata before external release.
- Restrictions: ["No standalone license for the derived hourly OHLC was located; treat it as derived from the Zenodo source and carry its CC BY 4.0 attribution conditions.", "Confirm the output contains only aggregate time/price/volume fields and not account identifiers or a reconstructable copy of raw event records.", "No specific venue prohibition on hourly OHLC reuse was located; this is not a representation that no such terms can apply."]
- Verification: derived-data rules based on retained Zenodo record snapshot; fresh upstream API/HTML fetch failed; venue-level restriction not verified; fresh authoritative DOI registry HTTP 200 confirms CC-BY-4.0, creators and title; accessed 2026-10-09T12:42:45Z
- Official sources: [source 1](https://creativecommons.org/licenses/by/4.0/), [source 2](https://hyperfoundation.org/), [source 3](https://www.hyperfoundation.us/termsOfService), [source 4](https://api.datacite.org/dois/10.5281/zenodo.18184441)
- Alternative: If the derived file includes only address-free OHLC rows, redistribute with a CC BY 4.0 attribution and modification notice after confirming the current Zenodo record license; otherwise use aggregate outputs that cannot expose participant identities.

### coinbase: Martin Søgaard Nielsen on Kaggle; dataset description says source messages came from Coinbase WebSocket order books

Kaggle metadata says CC0 and describes the corpus as originating from Coinbase WebSocket messages. Coinbase's current official Market Data Terms define order/transaction information as Market Data and restrict redistribution and AI/ML training. Their applicability to an already collected third-party copy is unresolved; the CC0 label cannot conclusively clear the underlying source rights.

- Redistribution: Kaggle's live dataset API labels the uploader's dataset CC0, which expresses a waiver for rights the uploader can waive. Coinbase's current Market Data Terms restrict third-party redistribution and derived works absent express written consent. Whether these terms bind a recipient who obtains a historical third-party Kaggle copy rather than accessing Coinbase Market Data directly, and whether the uploader owned/cleared all relevant rights, could not be established. Do not redistribute the raw corpus or derived market-data outputs until that rights conflict is resolved.
- Commercial use: CC0 permits commercial use without attribution for rights validly waived by the uploader. Coinbase Market Data Terms currently limit use to personal/research purposes and restrict redistribution and AI/ML training; their applicability to this third-party historical copy and any rights in the underlying data remain unclear. Treat commercial ML use as not cleared pending written permission/legal determination.
- Attribution: CC0 does not require attribution, though cite Martin Søgaard Nielsen and the Kaggle record for provenance. Coinbase terms do not create a general attribution substitute for required permission.
- Share-alike: No share-alike obligation under CC0.
- Derived data: Kaggle CC0 metadata purports to waive copyright/database rights held by the uploader, but may not waive Coinbase or third-party rights. Coinbase Market Data Terms define derived works broadly and restrict redistribution, display, or dissemination to third parties; they also prohibit use of Market Data to train, fine-tune, validate, benchmark, or improve AI/ML systems absent written consent. Because the file was sourced through Kaggle and historical terms at collection are not established, applicability must be resolved before sharing derived charts, features, or trained model artifacts.
- Restrictions: ["Live Kaggle metadata says CC0 Public Domain, but that alone does not confirm the uploader controlled all rights in Coinbase-origin data.", "Coinbase official Market Data Terms (current page accessed 2026-10-09) apply to Market Data made available by Coinbase; they restrict third-party redistribution and use for AI/ML training absent written consent.", "The precise contractual scope for a third-party recipient of the already-collected 2021 Kaggle corpus is unresolved; the market-data rights conflict is why the release classification is unclear.", "Do not rely on the separate Apache 2.0 license of a Kaggle notebook; it does not license this dataset."]
- Verification: live Kaggle API metadata verified (HTTP 200); Coinbase current Market Data Terms page captured; third-party-copy contract and rights scope unresolved; accessed 2026-10-09T12:38:12Z
- Official sources: [source 1](https://www.coinbase.com/legal/market_data), [source 2](https://www.coinbase.com/legal/developer-platform/terms-of-service), [source 3](https://creativecommons.org/publicdomain/zero/1.0/)
- Alternative: Use Coinbase data only under a direct written license that expressly allows commercial research, model training, and redistribution of specified derived outputs, or replace it with a source whose license and exchange rights clearly authorize those uses.

### yahoo: Yahoo Finance via yfinance

Yahoo indexed section 6(b) identifies its content/API IP and written-permission restriction; permissions guidance excludes third-party stock quotes from Yahoo's screenshot permission. yfinance's official README says its software license does not determine downloaded data rights.

- Redistribution: Do not redistribute without permission. Official indexed Terms section 6(b) requires explicit written permission for enumerated reproduction/distribution/exploitation uses; no redistribution grant for the local exports was found.
- Commercial use: No commercial data reuse grant verified; explicit written permission required for commercial exploitation under reviewed section 6(b).
- Attribution: Attribution alone does not supply permission. Preserve Yahoo and original exchange/provider identities in local records.
- Share-alike: No open share-alike license verified.
- Derived data: No general permission to redistribute adjusted bars, merged macro panels or recoverable transformations was verified. Treat derivatives as restricted pending permission.
- Restrictions: Yahoo/provider IP and API terms apply; no written permission supplied. yfinance software license does not license data. Source exchange entitlements and historical terms remain unverified.
- Verification: Official Yahoo Terms HTML captured HTTP 200 by public GET; sections 6(b), API license and automated-collection restrictions inspected. Direct web tool returned 999; acquisition-specific entitlements remain unverified.; accessed 2026-10-09T12:42:45Z
- Official sources: [source 1](https://legal.yahoo.com/us/en/yahoo/terms/otos/index.html?.intl=us&.lang=en-US), [source 2](https://legal.yahoo.com/us/en/yahoo/permissions/requests/index.html), [source 3](https://github.com/ranaroussi/yfinance)
- Alternative: Keep local-only references and lawful user-supplied input processing; request Yahoo and relevant exchange/provider redistribution rights. Do not publish a scraper that evades access restrictions.

### binance: Binance Vision

Official repository terms sections 1.4, 3 and 4 impose an NC/SA grant, attribution, commercial exclusions and conditions on derived data. Do not mistake this for an unrestricted public-domain dataset.

- Redistribution: Noncommercial redistribution with license, attribution and applicable obligations; exclude from the commercially reusable open-data release unless a separate written grant is obtained.
- Commercial use: No, absent separate written enterprise data license.
- Attribution: Binance Vision credit, license notice/link and changes notice; no endorsement or brand marketing implication.
- Share-alike: Redistributed adaptations must retain CC-BY-NC-SA-4.0.
- Derived data: The dataset terms expressly cover derived/calculated/extracted data. Aggregate bars and transformed selections do not remove NC/SA obligations.
- Restrictions: Noncommercial uses only; trading/commercial-product prohibitions; access/rate-limit compliance; third-party exceptions; no de-anonymization. Terms amendments apply prospectively; acquisition-time rights are not independently verified.
- Verification: official repository dataset-specific terms verified; supplemental website terms linked; historical grant unverified; accessed 2026-10-09T12:40:00Z
- Official sources: [source 1](https://github.com/binance/binance-public-data/blob/master/TERMS_AND_CONDITIONS.md), [source 2](https://www.binance.com/en/terms), [source 3](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)
- Alternative: Offer an explicitly separate noncommercial package only after NC/SA obligations and source notices are satisfied, or obtain written commercial permission. Current public selection excludes this family.

### fincast: Vincent05R / FinCast-Paper-test (underlying market suppliers UNVERIFIED)

Hugging Face dataset page identifies Apache-2.0. The minimal card provides no upstream provider rights schedule; Apache definitions limit licensor to owner/authorized licensor. No commercial market-data redistribution chain was established.

- Redistribution: Publisher's license label verified, but no per-vendor market redistribution permissions established. Exclude all raw and derived prices until the author provides the rights chain.
- Commercial use: Apache-2.0 normally permits commercial use of rights actually licensed; authority to sublicense underlying prices is unverified.
- Attribution: If cleared: retain original copyright/attribution and NOTICE material, include Apache-2.0, and mark changes.
- Share-alike: Apache-2.0 has no general share-alike; inherited third-party obligations still apply.
- Derived data: Daily resampling and canonical conversion do not establish independent market redistribution rights.
- Restrictions: Minimal dataset card contains a license label, not provenance/venue clearance. Apache grant covers only licensor-controlled rights and does not authorize third-party trademarks/data by itself. Hugging Face terms direct fetch returned 429.
- Verification: current publisher license metadata and Apache terms verified; upstream rights and hosting terms not fully verified; accessed 2026-10-09T12:40:00Z
- Official sources: [source 1](https://huggingface.co/datasets/Vincent05R/FinCast-Paper-test), [source 2](https://www.apache.org/licenses/LICENSE-2.0), [source 3](https://huggingface.co/terms-of-service)
- Alternative: Link to the original dataset and request supplier-by-supplier rights confirmation from its authors; retain local transformations without bundled raw prices.

### qlib: UNKNOWN upstream provider; local Qlib-compatible cn_data

Local binary layout identifies Qlib format only. Official Qlib documentation discusses alternate community data sources and Yahoo collection; neither authenticates this particular local archive.

- Redistribution: Not established; exclude.
- Commercial use: Not established.
- Attribution: UNKNOWN until original vendor/source and grant are supplied.
- Share-alike: UNKNOWN.
- Derived data: Qlib storage and software licensing do not establish data rights; do not redistribute feature vectors or reconstructed prices absent verification.
- Restrictions: Official Qlib README distinguishes software from third-party data and notes official data distribution is disabled. This does not prove that the local cn_data came from any particular vendor.
- Verification: software documentation verified; local dataset supplier/license UNKNOWN; accessed 2026-10-09T12:40:00Z
- Official sources: [source 1](https://github.com/microsoft/qlib)
- Alternative: Owner supplies acquisition URL and data license/permission. Publish a local input decoder only, with no data download vendor invented.

### unknown: UNKNOWN or multi-source local derivation

Discovery could not establish the vendor for Kronos fixture/Alibaba bars or the order-book sample. Model artifacts and copied submission bundles are not independent source datasets.

- Redistribution: No verified rights chain. Exclude from dataset release.
- Commercial use: UNKNOWN.
- Attribution: UNKNOWN; owner/source review required.
- Share-alike: UNKNOWN.
- Derived data: Predictions/metrics can contain reconstructible inputs or be governed by input contracts; origin, contributor ownership and leakage must be reviewed. No blanket derivative exception asserted.
- Restrictions: No sources invented from symbols or filenames; model benchmarks are outside this dataset-only paper's scope.
- Verification: UNVERIFIED source and permission; accessed 2026-10-09T12:40:00Z
- Official sources: 
- Alternative: Keep local-only; request provenance and contributor clearance. Release original code/documentation with licensed data examples from the cleared subset instead.

## Compatibility and release policy

MIT is recommended for original code, curation logic and documentation only. It is concise and permissive; Apache-2.0 adds an express patent grant and NOTICE obligations, while GPL imposes software copyleft. None can replace upstream data rights. Upstream CC-BY attribution must remain even when curation code is MIT. RBA Financial Data terms are separate and must not be mislabeled CC-BY. Public-domain agency material remains identified as such, without asserting a worldwide statutory result for every inclusion.

Binance NC/SA cannot be presented as a commercially reusable, permissively licensed combined dataset. Its derivative bars stay excluded from the main selection; an optional separately licensed noncommercial package is an owner decision. Yahoo, unresolved venue rights, unknown provenance and mixed tables with restricted inputs stay excluded. Filtering a mixed event file by independently attributable agency rows is logged and does not carry excluded FDIC records into the output. Aggregation alone is not presumed to cure restrictions.

Raw HTML/PDF source bodies and wallet-linked archives require artifact/notice or privacy review before inclusion; attribution alone does not satisfy those checks. The processed selection will include only structured agency facts and address-free aggregates with checked source identities, license notices and documented changes. A readable release manifest records which conditions have actually been satisfied.

## Audit checkpoint

The owner instructed completion of all requested local deliverables after approving discovery. This report is the audit checkpoint; remaining preparation is local only. No external push/upload or provider contact is approved. Permission-request drafts are unsent.
