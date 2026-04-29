# TNFD-disclosure · Nature-Related Financial Disclosure Workbench

> A traceable, evidence-based, phase-gated TNFD disclosure workflow for ESG consultants, sustainability teams, and AI Agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TNFD v1.0](https://img.shields.io/badge/TNFD-v1.0-blue)](https://tnfd.global)
[![ENCORE 2025.09](https://img.shields.io/badge/ENCORE-2025.09-green)](https://encorenature.org)
[![Validate](https://img.shields.io/badge/Claim%20Validation-10%2F10-brightgreen)](#fact-governance)

[**中文版**](README.md) · [**Quick Start**](#quick-start) · [**Workflow**](#workflow) · [**File Structure**](#file-structure) · [**Fact Governance**](#fact-governance)

---

## What This Solves

| Problem | How This Skill Addresses It |
|---|---|
| Scattered TNFD documentation | Integrated LEAP components, 14 recommendations, General Requirements, Metrics architecture |
| Unverifiable case figures | Claim Registry + `validate_claims.py` — pending claims cannot be stated as facts |
| Internal models misrepresented as official | All custom formulas labeled `method_status: internal`; not for external disclosure |
| Assurance language overreach | Outputs "assurance-readiness ratings", not audit opinions |
| China regulation conflated with TNFD | Clear separation: CSRC rules are mandatory; TNFD is voluntary |

---

## Workflow

```
Scope → Benchmark → Locate → Evaluate → Assess → Prepare → Assurance Readiness
  C1-C4    L1-L4      E1-E4    A1-A4    P1-P4
```

Each phase checks its evidence gate. When evidence is insufficient, the skill outputs a gap list instead of generating a "complete report".

### Commands

| Command | Purpose | Evidence Gate |
|---|---|---|
| `/tnfd` | Start assistant | None |
| `/tnfd new` | New project | Company + sector + reporting boundary |
| `/tnfd status` | Project state | Project state file |
| `/tnfd benchmark` | Industry benchmarking | None |
| `/tnfd locate` | Locate (C1-C4 + L1-L4) | Asset coordinates + supply chain layout |
| `/tnfd evaluate` | Evaluate (E1-E4) | ENCORE/BRF screening output |
| `/tnfd assess` | Assess (A1-A4) | LEAP output + financial data |
| `/tnfd prepare` | Prepare (P1-P4) | 14 recommendations + General Requirements check |
| `/tnfd audit` | Assurance readiness | All phase evidence |
| `/tnfd save` | Save state | None |
| `/tnfd reset` | Reset project | None |

---

## File Structure

```
TNFD-disclosure/
├── SKILL.md                        # Agent Skill definition (139 lines, v4 compliant)
├── prompts/                        # Phase prompts
│   ├── 00-benchmark.md             #   Phase 0: Benchmarking
│   ├── 01-locate.md               #   Phase 1: Locate
│   ├── 02-evaluate.md             #   Phase 2: Evaluate
│   ├── 03-assess.md                #   Phase 3: Assess
│   ├── 04-prepare.md              #   Phase 4: Prepare
│   └── 05-assurance.md            #   Phase 5: Assurance readiness
├── references/
│   ├── framework/                  # TNFD official framework references
│   │   ├── leap-components.md      #   C1-C4 / L1-L4 / E1-E4 / A1-A4 / P1-P4
│   │   ├── recommendations-14.md  #   14 recommendations + evidence request
│   │   ├── general-requirements.md  #   6 General Requirements gate
│   │   ├── metrics-architecture.md  #  Core / Sector / Additional / Comply-or-explain
│   │   └── value-chains.md         #   Upstream / downstream / traceability
│   ├── localization/
│   │   └── china-sustainability-reporting.md  # China regulatory mapping
│   └── sectors/
│       └── sector-guidance-index.json          # Sector guidance status index
├── data/
│   ├── case_claims_verification.json  # Claim Registry (12 pending)
│   ├── tnfd_report_links.json        # TNFD official report hub index
│   ├── encore_raw/                    # ENCORE raw data (2025.09)
│   └── encore_processed/             # Parsed data (48 ecosystem services × 21 industries)
├── scripts/
│   ├── tnfd_handler.py              # /tnfd command handler
│   ├── process_encore_data.py       # ENCORE data processing
│   ├── validate_claims.py           # Claim validator (CI ready)
│   └── smoke_test.sh                # Smoke test (4/4 passing)
└── assets/
    ├── tnfd-framework-infographic.png
    └── contact-qr.png               # Feishu QR for contact
```

---

## Fact Governance

All case references in this Skill are governed by the Claim Registry:

| Status | Meaning | Output Rule |
|---|---|---|
| `verified` | Registry has source URL + page | May be used as fact |
| `pending` | Leads exist but not verified | Only as "unverified leads" |
| `rejected` | Registry marks as unusable | Must not be output |

Current Registry: **12 pending**, scanned across 10 active files by `validate_claims.py`. No pending claim is currently used as a confirmed fact.

Run claim validation:
```bash
python3 scripts/validate_claims.py
```

---

## Quick Start

**Install**

```bash
git clone https://github.com/newversionparty-cn/TNFD-disclosure.git
cd TNFD-disclosure
ln -s $(pwd) ~/.Hermes/skills/tnfd-disclosure
```

**Smoke test**

```bash
bash scripts/smoke_test.sh
```

**Example session**

```
User: We're a Shenzhen Stock Exchange 100 constituent. Do we have to do TNFD in 2026?

TNFD-disclosure:
• Mandatory: CSRC requires 2025 annual sustainability report by 2026-04-30.
• TNFD itself is not mandatory in China, but can support voluntary alignment
  for nature/biodiversity disclosures.
• First determine whether your business has material nature-related topics.

User: Generate a complete TNFD report for me.

TNFD-disclosure:
• Evidence gate not met — "complete report" not generated.
• Recommended sequence: Scope → Benchmark → LEAP → Prepare → Assurance Readiness.
• What data do you have: asset coordinates, supply chain, ENCORE?
```

---

## Data Sources

| Source | Use | Status |
|---|---|---|
| [TNFD Recommendations v1.0](https://tnfd.global/recommendations/) | Framework basis | ✅ Official |
| [TNFD LEAP v1.1](https://tnfd.global/leap/) | Official component definitions | ✅ Official |
| [ENCORE 2025.09](https://encorenature.org) | Dependency/impact pathway data | ✅ Integrated |
| [WWF BRF](https://riskfilter.org/biodiversity) | Industry weighting + Exposure | ✅ Integrated |
| [TNFD Sector Guidance](https://tnfd.global/sector-guidance) | Sector-specific guidance | ⚠️ Verify per index |
| CSRC Sustainability Reporting Guidelines | China regulatory mapping | ✅ Integrated |
| CASS-ESG 6.0 | China local standard | ⚠️ Official verification pending |

---

## Disclaimer

This Skill provides methodological guidance and workflow support. **It does not constitute a formal audit or assurance opinion**.

- Does not claim any company's report "fully aligns with TNFD"
- Does not issue audit opinions, assurance opinions, "unqualified opinions", or "qualified opinions"
- All case figures require source and page citation, or must be labeled as pending verification
- Custom scoring models must not be presented as official TNFD metrics

For formal disclosures, complete LEAP assessment and consult qualified professionals.

---

## Contact

For TNFD disclosure consulting needs or collaboration:

<div align="center">

![Feishu QR](./assets/contact-qr.png)

**Scan to connect · Note "TNFD"**

</div>

---

*Maintainer: [Tom](https://github.com/newversionparty-cn) · Issues & PR welcome*
