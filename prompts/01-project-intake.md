# Prompt 01: Project Intake

> Use to turn beginner answers into a structured LEA project record.

## Inputs To Collect

Ask no more than 5 at once:

1. Company name
2. Business description
3. Sector or product/service
4. Main sites or cities
5. Analysis purpose
6. Direct operations only or value chain included
7. Available data: addresses, coordinates, suppliers, water, emissions, waste, financials

## Output Schema In Markdown

```markdown
## Partner Brief
合伙人，先给结论：当前项目可以进入 {low/medium/high}-data LEA analysis.

## Intake Workpaper
| Field | Value | Confidence | Gap |
|---|---|---|---|
| Company | ... | high/medium/low | ... |
| Sector | ... | high/medium/low | ... |
| Boundary | direct operations / value chain / unknown | ... | ... |
| Purpose | ... | ... | ... |
| Data maturity | low/medium/high | ... | ... |

## Big4 Lens
| Stage | Lens | Why |
|---|---|---|
| Intake | PwC Readiness lens | Beginner-friendly scoping |
| Locate | Deloitte Diagnostic lens | Asset/location data integration |
| Evaluate | KPMG Materiality lens | Prioritise dependencies and impacts |
| Assess | EY Financial Pathway lens | Translate to business risk and opportunity |

## Partner Challenge Checklist
| Check | Pass? | Note |
|---|---|---|
```
