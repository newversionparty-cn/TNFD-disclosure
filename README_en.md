# TNFD-disclosure

> 🌍 Making Nature-related Financial Disclosures as accessible as TCFD. | [中文版](./README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TNFD Version](https://img.shields.io/badge/TNFD-v1.0-blue)](https://tnfd.global)
[![ENCORE Version](https://img.shields.io/badge/ENCORE-2025.09-green)](https://encorenature.org)
[![Platform](https://img.shields.io/badge/Platform-Hermes%7CClaude%20Code%7COpenClaw-blueviolet)](https://github.com/newversionparty-cn/TNFD-disclosure)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

## What is this?

**TNFD-disclosure is an AI Agent Skill (Prompt Library), not a Python CLI or Web App.**

It is a structured prompt + knowledge base package designed for AI agents that support custom skills — specifically Hermes, Claude Code, and OpenClaw.

| If you are... | How to use |
|---------------|------------|
| **ESG Consultant** | Use `SKILL.md` content as your AI Agent's System Prompt |
| **Developer** | Reference modular Prompt templates in `prompts/` to integrate into your Agent |
| **AI Agent User** | Install this package in a Skill-enabled Agent and type `/tnfd` to activate |

---

## Architecture

```
TNFD-disclosure/
├── SKILL.md              # Main Skill file (System Prompt + Knowledge Base)
├── QUICK_REFERENCE.md    # Agent quick reference card
├── prompts/              # Modular Prompt templates
│   ├── 00-benchmark.md    # Phase 0: Benchmarking
│   ├── 01-locate.md       # Phase 1: Locate
│   ├── 02-evaluate.md    # Phase 2: Evaluate
│   ├── 03-assess.md       # Phase 3: Assess
│   ├── 04-prepare.md      # Phase 4: Prepare
│   └── 05-assurance.md    # Phase 5: Assurance
├── references/           # Reference knowledge base
│   ├── tnfd-leap-complete-guide.md
│   ├── big4-methodologies.md
│   ├── china-esg-standards.md
│   └── ...
├── data/                 # Built-in data
│   ├── encore_processed/ # ENCORE processed JSON (Sep 2025)
│   └── tnfd_report_links.json
└── scripts/
    ├── tnfd_handler.py    # State manager (optional)
    └── process_encore_data.py
```

### Workflow

```
Phase 0          Phase 1: LEAP                    Phase 2
  │              ┌──┬───┬────┬────┐               │
  ▼              │L │ E │  A │  P │               ▼
Benchmarking ──► └──┴───┴────┴────┘ ─────────► Assurance
  │              (Locate→Evaluate→Assess→Prepare)  │
  ▼                                                ▼
Case Studies ───────────────────────────────► Report Generation
```

---

## Quick Start

### Step 1: Install the Skill

**Hermes (Recommended)**
```bash
ln -s ~/Desktop/TNFD/skill ~/.Hermes/skills/tnfd-disclosure
```

**OpenClaw**
```bash
cp -r ~/Desktop/TNFD/skill ~/.openclaw/skills/tnfd-disclosure
```

**Claude Code**
```bash
mkdir -p ~/.claude/skills && cp -r ~/Desktop/TNFD/skill ~/.claude/skills/tnfd-disclosure
```

### Step 2: Activate the Skill

In any Skill-enabled Agent conversation, type:
```
/tnfd
```

The Agent will display a Sprint Banner and enter the TNFD workflow.

### Step 3: Start a Project

```
/tnfd new                           # New project
/tnfd benchmark                     # Phase 0: Benchmarking
/tnfd locate                       # Phase 1: Locate
/tnfd evaluate                      # Phase 2: Evaluate
/tnfd assess                        # Phase 3: Assess
/tnfd prepare                       # Phase 4: Prepare
/tnfd audit                         # Phase 5: Assurance
/tnfd report                        # Generate report
```

---

## TNFD LEAP Framework

TNFD v1.0 (published September 2023) is built on the **LEAP methodology**:

| Phase | English | Core Question | Primary Data Sources |
|-------|---------|---------------|----------------------|
| **L** | Locate | Where are your assets? Are these locations ecologically sensitive? | WDPA, IBAT, WRI Aqueduct, Ecological Red Lines |
| **E** | Evaluate | Which natural capital do your operations depend on? What impacts do you have? | **WWF BRF + ENCORE** (three-layer system) |
| **A** | Assess | Can these dependencies and impacts be translated into financial figures? | NGFS Framework + Replacement Cost Method |
| **P** | Prepare | How to disclose? Do you meet all 14 TNFD Recommendations? | TNFD v1.0 Disclosure Template |

### Assess Phase — Quantification Maturity Levels

| Level | What You Can Do | Skill Can Guide You |
|-------|-----------------|---------------------|
| L1 (Basic) | Qualitative risk identification | ✅ Yes |
| L2 (Intermediate) | Semi-quantitative (area, volume) | ✅ Yes |
| L3 (Advanced) | Financial equivalent quantification | ⚠️ Methods provided, not precise figures |
| L4 (Exact) | Requires client ERP data | ❌ Skill cannot replace |

> ⚠️ **Skill Boundary**: The Skill is a "GPS navigator", not a "driver". Precise financial quantification requires client internal data — no Agent can replace that.

---

## Data Sources

| Data Source | Use Case | LEAP Phase | Free? | Notes |
|-------------|----------|------------|-------|-------|
| **WWF BRF** | Industry dependency/impact weights (primary) + Exposure | E | ✅ Free | [官网](https://riskfilter.org/biodiversity) |
| **ENCORE** | Dependency/Impact pathway (base layer) | E, A | Basic free | [官网](https://encorenature.org) |
| **WDPA** | Protected Area Database | L | Free | UNEP-WCMC |
| **IBAT** | Integrated Biodiversity | L, E | Research free | Commercial requires subscription |
| **WRI Aqueduct** | Water Risk Atlas | L, A | Free | [官网](https://www.wri.org/aqueduct) |
| **Ecological Red Lines** | China's Ecological Sensitive Zones | L | Non-public | Apply via Ministry of Natural Resources |
| **Blue Map (IPE)** | Corporate Pollution Records | L, E | Partially free | [IPE](https://www.ipe.org.cn) |

---

## China Context

**TNFD Status in China**:
- CSRC 2024 issued the "Listed Company Sustainability Report Guidelines" — **not identical to TNFD**
- The 2026 A+H mandatory requirement applies to these Guidelines, not TNFD itself
- TNFD remains in **voluntary adoption** phase in China
- Leading adopters: LONGi Green Energy (Nov 2025), Muyuan Foods (Mar 2026)

**Local Standards Reference**:
- CASS-ESG 6.0 (China-EU alignment version)
- CSRC "Listed Company Sustainability Report Guidelines" (2024)
- MEE "Enterprise Environmental Information Disclosure Management Measures"

---

## Core Features

### Phase 0: Benchmarking

Input industry name → Match benchmark cases (LONGi / Muyuan / HSBC / Rio Tinto) → Output gap analysis framework

### Phase 1–4: LEAP Assessment

- **L – Locate**: Asset coordinates → ecological sensitivity overlay analysis
- **E – Evaluate**: Industry classification → ENCORE dependency/impact matrix
- **A – Assess**: Risk quantification + opportunity identification
- **P – Prepare**: TNFD report preparation

### Phase 5: Assurance

Coverage check across all 14 TNFD Disclosure Recommendations (Governance 2 + Strategy 2 + Risk & Impact Management 4 + Metrics & Targets 6)

---

## Benchmark Cases

### LONGi Green Energy (Solar PV)

**Report Info**:
- Publication: November 2025 (COP30)
- Report Type: Independent TNFD Report
- Methodology: TNFD LEAP + EY CCaSS

**Key Highlights**:
- 🏆 China's first independent TNFD report by a solar PV company
- 💰 Natural capital assessment pilot (Jiaxing base saved ¥21.496M)
- 🎯 2050 Biodiversity "Net Zero Loss" target
- 🌿 2060 Nature "Net Positive Impact" vision

| Metric | Data |
|--------|------|
| LEAP Completeness | 4/4 phases complete |
| 14-Item Coverage | 10/14 (71%) |

### Muyuan Foods (Aquaculture)

**Report Info**:
- Publication: March 2026 (HKEX)
- Methodology: TNFD LEAP + Deloitte + Natural Capital Protocol

**Monitoring System**:

| Category | Indicators | Frequency |
|----------|-----------|-----------|
| Soil | 16 | 2x/year × 100% coverage |
| Groundwater | 12 | 2x/year × 100% coverage |
| Surface Water | 6 | 1–4x/year |
| Agricultural Products | 15 | 1–2x/year |

---

## Methodology Framework

### Big Four TNFD Methodologies

| Firm | Methodology | Core Keywords |
|------|-------------|---------------|
| **EY** | CCaSS | Natural Capital Monetization / Financial Integration / IUCN Partnership |
| **Deloitte** | Climate & Sustainability | Digital Monitoring / Circular Economy / Natural Capital Protocol |
| **PwC** | Five Things | 5-Step Framework / Checklist / Disclosure Template |
| **KPMG** | NATURE Framework | Maturity Assessment / Phased Implementation / Roadmap Planning |

> ⚠️ Big Four methodology references are based on public sources. For details, refer to each firm's official TNFD whitepaper. **⚠️ Verification status: Pending.**

### Official References

| Document | Source | URL |
|----------|--------|-----|
| TNFD v1.0 Recommendations (Official) | TNFD | [PDF](https://tnfd.global/wp-content/uploads/2023/08/Recommendations-of-the-Taskforce-on-Nature-related-Financial-Disclosures.pdf) |
| TNFD LEAP Complete Guide | TNFD | [Link](https://tnfd.global/publication/additional-guidance-on-assessment-of-nature-related-issues-the-leap-approach/) |
| ENCORE Database | UNEP FI + Global Canopy | [Link](https://encorenature.org) |
| IBAT Integrated Biodiversity Tool | BirdLife/IUCN/Conservation International/UNEP-WCMC | [Link](https://www.ibat-alliance.org) |
| WRI Aqueduct Water Risk Atlas | World Resources Institute | [Link](https://www.wri.org/aqueduct) |
| NGFS Nature-related Financial Risk Framework | Central Banks & Supervisors Network | [Link](https://www.ngfs.fr) |

---

## File Structure

```
TNFD-disclosure/
├── SKILL.md                    # Main Skill file
├── QUICK_REFERENCE.md          # Agent quick reference
├── CHANGELOG.md                # Version history
├── prompts/                    # Modular Prompts
│   ├── 00-benchmark.md         # Benchmarking
│   ├── 01-locate.md           # Locate phase
│   ├── 02-evaluate.md         # Evaluate phase
│   ├── 03-assess.md           # Assess phase
│   ├── 04-prepare.md          # Prepare phase
│   └── 05-assurance.md         # Assurance phase
├── references/                 # Knowledge base
│   ├── tnfd-leap-complete-guide.md
│   ├── big4-methodologies.md
│   ├── china-esg-standards.md
│   └── ...
├── data/                       # Built-in data
│   ├── encore_processed/       # ENCORE JSON
│   └── tnfd_report_links.json
└── scripts/
    └── process_encore_data.py
```

---

## Contribution Guidelines

Issues and Pull Requests welcome!

**Pre-submission Checklist**:
- [ ] Methodology citations include sources
- [ ] Data sources marked as free/paid
- [ ] No statistics fabricated from memory
- [ ] New Prompts tested before submission

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Appendix: China vs. International TNFD Status

| Dimension | China | International |
|-----------|-------|---------------|
| **Regulatory Requirement** | Voluntary (Guidelines ≠ TNFD) | G20 push, ISSB referenced |
| **Adopting Organizations** | Leading pioneers (LONGi, Muyuan) | 416+ organizations (as of Dec 2025) |
| **Data Environment** | Ecological Red Lines non-public | WDPA/IBAT free/subscription |
| **Methodology** | CASS-ESG 6.0 alignment | ENCORE + LEAP |
| **Assurance Requirement** | No mandatory third-party assurance | TNFD provides assurance guidance |

> 📊 Data sources: TNFD official (tnfd.global), IPE (Blue Map), CSRC official website (csrc.gov.cn)

---

*Last updated: 2026-04-20*
