# ENCORE + IBAT LEAP Use Guide

Purpose: tell the agent when to use ENCORE and IBAT during beginner LEA work, what each source can support, and what it must not claim.

Last reviewed: 2026-04-30

## Source Boundary

| Tool | What it is | Best LEAP fit | Do not use it for |
|---|---|---|---|
| ENCORE | Public online tool and knowledge base for economic activities' dependencies and pressures on nature | Evaluate, with Intake support and Assess inputs | Site-specific biodiversity evidence, official TNFD risk score, monetary quantification |
| IBAT | Authoritative biodiversity data access and screening platform for IUCN Red List, WDPCA/WDPA + WD-OECM, WDKBA, STAR, and rarity-weighted richness | Locate, with Evaluate context and Assess risk inputs | Bulk scraping, unlicensed site reports, substituting for site surveys or legal ecological due diligence |

## ENCORE Officially Supported Analysis

Use ENCORE when the user provides a sector, product, business activity, ISIC code, or high-level business description.

ENCORE supports:

- Economic activity to ecosystem service dependency screening.
- Economic activity to pressure / impact-driver screening.
- Materiality ratings for dependency and pressure links on a five-point scale.
- ISIC-based activity mapping and some crosswalk support.
- Upstream and downstream links when the local ENCORE files are available.

Local data available in this Skill:

| Local file | Use |
|---|---|
| `data/encore_raw/03. Dependency links.csv` | Dependency narratives by ISIC activity and ecosystem service |
| `data/encore_raw/05. Pressure links.csv` | Pressure / impact-driver narratives by ISIC activity |
| `data/encore_raw/06. Dependency mat ratings.csv` | VH/H/M/L/VL dependency materiality ratings |
| `data/encore_raw/07. Pressure mat ratings.csv` | VH/H/M/L/VL pressure materiality ratings |
| `data/encore_raw/14. EXIOBASE NACE ISIC crosswalk.csv` | Crosswalk support for activity classification |
| `data/encore_processed/*.json` | Fast lookup summaries for the agent |

Official boundary:

- ENCORE's knowledge base is not location-specific. The agent must not use ENCORE alone to claim a particular site is in or near a sensitive ecosystem.
- ENCORE materiality means significant or important for decision-making in the ENCORE screening context; it is not the same as fiduciary, regulatory, financial, or TNFD disclosure materiality.
- ENCORE identifies typical dependencies and pressures. Actual importance changes with company process, site location, value chain, mitigation controls, and stakeholder context.
- If the user has no ISIC code, infer candidate ISIC activity from the business description, mark it as an internal classification assumption, and ask for confirmation.

## IBAT Public And Licensed Data Boundary

Use IBAT when the user provides site addresses, coordinates, a concession/project area, supplier locations, or a need to assess proximity to biodiversity-sensitive locations.

IBAT supports:

- Protected and conserved area screening via WDPCA / WDPA + WD-OECM.
- Key Biodiversity Area screening via WDKBA.
- Species sensitivity context using IUCN Red List data.
- STAR and rarity-weighted richness as derived biodiversity layers, where available under the user's access rights.
- Reports and GIS downloads depending on the user's subscription or pay-as-you-go access.

Public website data can be used to explain what IBAT contains and why it is relevant. Site-level IBAT reports, raw GIS downloads, API results, and derived layers must only be used if the user provides licensed outputs or credentials and the use complies with the applicable terms.

Do not scrape paywalled IBAT reports, app data, map tiles, GIS downloads, API responses, or derived datasets. If the user has no licensed IBAT output, create only an evidence request:

```markdown
| Evidence needed | Why | Minimum acceptable input |
|---|---|---|
| IBAT proximity report or licensed GIS extract | Supports Locate L4 sensitive-location screen | Site coordinates plus IBAT report/GIS output, date, buffer, and license status |
```

## LEAP Step Mapping

### Intake / Scope

| Question | ENCORE use | IBAT use |
|---|---|---|
| What business activity are we analysing? | Map business description to candidate ISIC / activity | Not primary |
| Which assets and value-chain nodes matter? | Identify activities likely to have high dependency or pressure pathways | Identify which locations need site-level biodiversity screening |
| What data is missing? | ISIC, production process, raw materials, supplier activity | Coordinates, asset boundary, buffer, IBAT report/GIS evidence |

### Locate

ENCORE role: secondary screen only. Use it to flag which activity-location combinations deserve more attention.

IBAT role: primary biodiversity-sensitive location input when licensed site data exists.

Required Locate language:

```markdown
ENCORE flags the activity's typical nature interface. It does not prove site-level sensitivity.
IBAT / WDPA / WDKBA evidence is needed for protected area, KBA, threatened species, STAR, or rarity-weighted richness screening.
```

Locate deliverable additions:

| Field | Description |
|---|---|
| IBAT evidence status | none / public source only / user-provided report / licensed GIS |
| Biodiversity sensitivity source | IBAT, Protected Planet, KBA, IUCN Red List, local EIA, or user evidence |
| Spatial confidence | city-only / address / coordinates / GIS boundary |

### Evaluate

ENCORE role: primary first-pass dependency and impact source.

IBAT role: location context that can raise or lower the priority of ENCORE-identified pressures.

Required Evaluate language:

```markdown
This dependency / pressure matrix uses ENCORE as a sector screening source and IBAT or other spatial sources as location context where available. It is not an official TNFD risk score.
```

Evaluate deliverable additions:

| Business activity | ENCORE dependency | ENCORE pressure | ENCORE rating | IBAT/location modifier | Evidence status |
|---|---|---|---|---|---|

### Assess

ENCORE role: convert dependencies and pressures into risk drivers.

IBAT role: support risk trigger evidence for sensitive locations, regulatory attention, critical habitat, reputation, project permitting, and mitigation prioritisation.

Required Assess language:

```markdown
Financial impact pathways are hypotheses until supported by site financials, permits, production data, contracts, or user-provided loss/cost evidence.
```

Assess examples:

| Risk pathway | ENCORE input | IBAT input | Financial pathway |
|---|---|---|---|
| Water dependency disruption | Water supply / water flow dependency | Site in water-sensitive or protected ecosystem context if evidenced | Downtime, water cost, capex for recycling |
| Land-use impact pressure | Area of land use pressure | KBA / protected area proximity if evidenced | Permitting delay, mitigation cost, capex redesign |
| Species or habitat sensitivity | Disturbance / pollution pressure | IUCN Red List / KBA / STAR evidence if licensed | Compliance cost, reputational risk, project delay |

### Prepare

Use ENCORE and IBAT as evidence appendices only after Locate, Evaluate, and Assess outputs are clear. Do not make external disclosure claims from screening data alone.

Prepare evidence table:

| Disclosure use | Allowed if | Required caveat |
|---|---|---|
| Describe methodology | Source, date, method and limitations are recorded | Screening tool, not assurance evidence by itself |
| Identify priority issues | Supported by user evidence and tool outputs | Requires management review and evidence owner |
| Report site sensitivity | Licensed IBAT/GIS output or authoritative public spatial source exists | Method, buffer, date, and limitations disclosed |

## Combined Beginner Workflow

1. Start with user business description and site list.
2. Map business activity to candidate ISIC using ENCORE crosswalk or internal classification assumption.
3. Generate a low-data ENCORE dependency / pressure matrix for Evaluate.
4. Ask for coordinates or asset boundaries for Locate.
5. If the user has IBAT or public spatial evidence, add biodiversity sensitivity; otherwise mark `IBAT evidence pending`.
6. Translate ENCORE pathways plus IBAT/location evidence into Assess risk and opportunity pathways.
7. Do not quantify money unless the user provides financial data.

## Partner Challenge Checklist

| Check | Pass condition |
|---|---|
| ENCORE boundary clear | Stated as sector/activity screening, not site proof |
| IBAT boundary clear | No paywalled data scraping; licensed output required for site claims |
| LEAP step correct | ENCORE mainly Evaluate; IBAT mainly Locate |
| Low-data version produced | Matrix/register exists even when data is incomplete |
| Evidence gaps explicit | Coordinates, ISIC, IBAT report/GIS, financials listed separately |

## Source List

- ENCORE methodology: https://encorenature.org/en/data-and-methodology/methodology
- ENCORE materiality: https://encorenature.org/en/data-and-methodology/materiality
- ENCORE limitations: https://encorenature.org/en/data-and-methodology/limitations
- IBAT data: https://www.ibat-alliance.org/data
- IBAT about: https://www.ibat-alliance.org/about
- IBAT pricing and access options: https://www.ibat-alliance.org/pricing
