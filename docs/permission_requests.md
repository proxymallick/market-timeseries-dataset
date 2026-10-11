# Unsent permission-request drafts

**These are drafts. I have not sent them or contacted any provider.** They ask for clarification or permission; they do not assume that a provider must grant either. Sending one requires a separate decision.

Each request should name the actual source, fields, period, transformations, and intended distribution. It should cover commercial and non-commercial research, raw and transformed redistribution, public hosting, historical vintages, aggregates, and ML training or evaluation. It should also ask whether a separate license is required and whether the answer covers third-party rights.

## 1. Yahoo Finance futures exports and derivatives

**Route:** Yahoo's [permissions request page](https://legal.yahoo.com/us/en/yahoo/permissions/requests/index.html). I have not added an unverified email address. The final request needs the exchange, provider, account, and acquisition context; yfinance is software, not the data licensor.

> Subject: Permission request for historical Yahoo Finance futures data and derived research tables
>
> Hello Yahoo Permissions Team,
>
> I am preparing a research dataset containing historical continuous futures price exports obtained through Yahoo Finance. Before any external distribution, I would like to determine whether Yahoo can grant permission for the specific source records and proposed outputs described below. The collection and acquisition dates are [dates/method/account context]. The instruments and fields are [list]. The prepared transformations include [adjustment/resampling/merging/derived fields]. The intended use is [commercial/non-commercial research, model development or other specified use].
>
> Could you confirm whether written permission is available for (1) redistribution of the historical source records, (2) publication and redistribution of derived/resampled tables and aggregate results, and (3) use of the data for training, fine-tuning, validation, or benchmarking machine-learning models? Please identify any required attribution, volume limits, provider/exchange approvals, or separate license terms. If Yahoo is not the rights holder for any of these fields, please identify the appropriate source or rights holder if known.
>
> No data will be published unless the required permissions are established.
>
> Regards,  
> Prakash Mallick

## 2. FinCast-Paper-test authors / dataset publisher

**Route:** the dataset host's official contact or discussion channel. I found no verified author email, so I have not invented one. The request needs a provider-by-provider rights schedule, not another copy of the repository license label.

> Subject: Request for source rights and market-data provenance for FinCast-Paper-test
>
> Hello FinCast dataset maintainers,
>
> I am reviewing a local copy of FinCast-Paper-test and its derived daily, PCIE, and zero-shot tables. The dataset page identifies an Apache-2.0 license, but the locally available card does not establish the upstream market-data rights chain. Could you provide the original data sources/vendors for each market segment and period, the applicable acquisition agreements or licenses, and confirmation that the licensor had authority to permit redistribution and commercial use?
>
> In particular, does the grant cover redistribution of source records, daily/resampled and other derived tables, aggregates, public repository or data-host distribution, and use for commercial ML training, fine-tuning, validation, and benchmarking? Please identify required notices, attribution, share-alike or downstream terms, venue limits, and any dataset components that are excluded from the publisher's license.
>
> I will keep the local copy out of any external release until these questions are resolved.
>
> Regards,  
> Prakash Mallick

## 3. FI-2010 authors and Nasdaq Helsinki rights holder

**Route:** verified institutional or publication contacts for the FI-2010 authors, plus Nasdaq's official European market-data licensing channel. I have not inferred individual or sales addresses. The request must address both the Fairdata CC BY record and the exchange-origin rights.

> Subject: FI-2010 redistribution and source-venue rights clarification
>
> Dear FI-2010 authors and Nasdaq licensing team,
>
> I am evaluating a local FI-2010 copy for a possible research dataset. The Fairdata record labels the dataset CC BY 4.0 and identifies creators including Adamantios Ntakaris, Martin Magris, Juho Kanniainen et al.; the data are described as originating from Nasdaq Helsinki. The current Nasdaq European Data Policies refer to restrictions on redistribution of subscriber-sourced historical data above five order-book levels. I have not established whether those terms govern this publisher-authorized historical benchmark or whether the original venue rights were cleared.
>
> Could you clarify: (a) who supplied the venue data and under what agreement; (b) whether the creators had authority to grant CC BY 4.0 for all 10 levels and associated records; (c) whether commercial redistribution, publication, derived features/aggregates, and model training/validation are permitted; and (d) whether the September 2026 venue policy or an earlier historical policy applies to this released benchmark? Please state any attribution, retention, transformation, and share-alike requirements.
>
> Please identify any elements that are outside the grant. No FI-2010 material will be externally distributed unless the applicable rights are established.
>
> Regards,  
> Prakash Mallick

## 4. Coinbase market data / Kaggle third-party copy

**Verified contact:** `marketdata@coinbase.com`, listed in Coinbase's [Market Data Terms](https://www.coinbase.com/legal/market_data) on 2026-10-09. This request concerns the historical Kaggle copy and does not assume that direct Coinbase terms bind every third-party recipient.

> To: marketdata@coinbase.com  
> Subject: Rights clarification for historical Coinbase WebSocket order-book dataset obtained via Kaggle
>
> Hello Coinbase Market Data Team,
>
> I am reviewing the Kaggle dataset “High Frequency Crypto Limit Order Book Data” by Martin Søgaard Nielsen, which its page labels CC0 and describes as derived from Coinbase WebSocket order-book messages (dataset page: https://www.kaggle.com/datasets/martinsn/high-frequency-crypto-limit-order-book-data). I did not receive this corpus directly from Coinbase. I am trying to determine whether the uploader's CC0 label is sufficient for the underlying data and whether Coinbase's Market Data Terms apply to downstream recipients of this historical third-party copy.
>
> Could Coinbase confirm whether it or another party controls rights in the source records and whether written permission can cover commercial research; redistribution of raw or derived order-book data and aggregate outputs; public hosting; and training, fine-tuning, validation, or benchmarking machine-learning systems? Please specify whether permission could apply to historical data already collected by a third party, what data levels/fields and transformations it covers, and any attribution, deletion, or downstream-license requirements.
>
> I will not redistribute this dataset or derived market-data outputs while the rights question remains unresolved.
>
> Regards,  
> Prakash Mallick

## 5. Qlib archive / unknown original provider

**Route:** none until I identify the original provider. A Qlib-compatible layout does not show that Microsoft supplied or licensed the data. First inspect the original download, invoice, README, or provider manifest; then contact the named rights holder.

> Subject: Rights and provenance request for Chinese-equity feature archive
>
> Hello [identified provider or rights holder],
>
> I am reviewing a local Chinese-equity feature archive stored in a Qlib-compatible format. I have not yet established the original data provider, acquisition method, or governing license. The archive appears to contain [verified instruments/fields/period once determined].
>
> Please confirm whether your organization supplied or controls this data, the applicable agreement and terms on the acquisition date, and whether the following are permitted: local analytical use; redistribution of raw features or source observations; redistribution of derived or aggregated tables; commercial research; machine-learning training, fine-tuning, validation, and benchmarking; and public repository or data-host distribution. Please identify any provider-sourced components, restrictions, attribution or retention conditions, and whether a separate written license is required.
>
> No external distribution is planned until the provider and rights are identified and the requested scope is confirmed.
>
> Regards,  
> Prakash Mallick

## 6. U.S. Treasury daily yields and FDIC Failed Bank List

**Route:** each agency's official contact form, with the exact download page named. I have not verified an agency email address. These are separate products and should be asked about separately.

### Treasury daily par-yield curve rates

> Subject: Reuse terms for downloadable daily Treasury par-yield curve rates
>
> Hello,
>
> I am reviewing the daily par-yield curve CSV/XML data published at https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?page=0&type=daily_treasury_yield_curve and described at https://home.treasury.gov/treasury-daily-interest-rate-xml-feed. The pages establish data availability but the terms reviewed do not state a dataset-specific redistribution grant.
>
> Could you confirm whether historical daily rates may be copied and redistributed, including commercially, and whether derived/resampled series, aggregates, and machine-learning training/validation uses are permitted? Please identify any license, attribution, source notice, fee, or downstream restriction and whether the answer covers these exact downloadable tables.
>
> Regards,  
> Prakash Mallick

### FDIC Failed Bank List

> Subject: Reuse terms for the FDIC Failed Bank List data download
>
> Hello,
>
> I am reviewing the downloadable data from the FDIC Failed Bank List at https://www.fdic.gov/bank-failures/failed-bank-list. The page provides a download, but I have not established dataset-specific reuse terms. The separate FDIC Archive copyright information does not clearly state that it governs this listing.
>
> Could you confirm whether the Failed Bank List download may be copied and redistributed, including commercially, and whether derived tables, aggregate statistics, and machine-learning research uses are permitted? Please identify applicable attribution, disclaimer, source notice, and any restrictions, and clarify whether the Archive policy applies to this separate data product.
>
> Regards,  
> Prakash Mallick

## 7. Binance Vision commercial redistribution

**Route:** the official Binance public-data repository's contact channel. I have not verified a recipient email. The current CC BY-NC-SA 4.0 terms do not clear the material for a commercially reusable combined release.

> Subject: Permission for commercial redistribution and ML use of Binance Vision historical data
>
> Hello Binance public-data team,
>
> I hold historical Binance Vision archives covering [verified instruments, fields and acquisition dates]. The current repository terms specify CC BY-NC-SA 4.0. Could you confirm the governing terms at acquisition and whether a separate written license can permit commercial redistribution of these records, derived or aggregated tables, and machine-learning training, validation and benchmarking? Please specify attribution, downstream terms, exchange/provider rights and public-hosting limits. The files will remain outside the proposed release unless the necessary permission is established.
>
> Regards,  
> Prakash Mallick

## Follow-up record

If I send a request later, I will record the date, recipient, channel, exact wording, response, attachments, and license terms in the audit evidence. Silence is not permission. Any written answer needs a scope and authority review before I change the release selection.
