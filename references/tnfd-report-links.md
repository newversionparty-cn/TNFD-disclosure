# TNFD Report Links And Candidate Case Leads

> Purpose: Use for benchmark discovery only. This file is not a verified case database.

## Evidence Rule

All company rows in this file are candidate leads. Before using a report date, report type, methodology, coverage rate, monetary figure, or assurance statement as a fact, check `data/case_claims_verification.json`.

Use this wording if not yet verified:

> The local case registry contains a pending case lead for {company}. The claim requires source URL and page-level verification before it can be used as a verified benchmark.

TNFD's example reporting hub provides illustrative examples and does not by itself mean TNFD endorses a report or confirms full alignment with all 14 recommendations.

## Official Hub

- TNFD example reporting hub: https://tnfd.global/knowledge-hub/example-tnfd-reporting/

## Candidate Leads By Sector

| Sector | Candidate companies | Status |
|---|---|---|
| Solar / clean energy | LONGi, GCL, Vestas, AMEA Power, Orsted, CELSIA COLOMBIA | Pending verification |
| Agriculture / food / livestock | Muyuan, Agrovision, New Hope Liuhe, Bunge, Charoen Pokphand Group, Akita Satoyama Design | Pending verification |
| Financial institutions | HSBC, Standard Chartered, Commerzbank, Banco de Bogota, Banco Bolivariano, Bank Australia, Amundi, Candriam, AP7, AP2, Cathay Financial Holding, CTBC Financial Holding, E.SUN Financial Holding | Pending verification |
| Metals / mining / materials | Rio Tinto, BHP, Endeavour Mining, CSN, Asia Cement Corporation, Cementos Argos | Pending verification |
| Real estate / construction | Brigade Enterprises, City Developments Limited, Covivio, Forico | Pending verification |

## Benchmark Output Template

```markdown
| Company | Sector | Claim status | Verified source | Report page | Usable benchmark lesson |
|---|---|---|---|---|---|
| LONGi | Solar / clean energy | pending | missing | missing | Do not use yet |
```

## Quarterly Maintenance Checklist

1. Open the TNFD official hub.
2. Search each candidate company.
3. Download or open the official report.
4. Record source URL, publication date, report page, and exact claim.
5. Update `data/case_claims_verification.json`.
6. Only then upgrade claim status from `pending` to `verified`.
