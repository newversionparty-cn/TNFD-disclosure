# Prompt 02: Locate Wizard

> Use for beginner-friendly Locate analysis. The user may only have cities or addresses.

## Data Levels

| Level | User evidence | Allowed conclusion |
|---|---|---|
| L0 | City only | City-level screening only |
| L1 | Address | Site-level draft, coordinates missing |
| L2 | Coordinates | Location-specific screening possible |
| L3 | GIS or supplier coordinates | Advanced spatial analysis possible |

## ENCORE / IBAT Guidance

- Use IBAT, WDPCA/WDPA, WDKBA/KBA, IUCN Red List, STAR or rarity-weighted richness evidence for biodiversity-sensitive location screening only when the user provides coordinates, boundaries, reports, GIS output, or other licensed/public spatial evidence.
- Do not scrape IBAT app outputs, paid reports, API results, map tiles, GIS downloads, or derived datasets.
- If the user only provides city-level data, mark IBAT status as `evidence pending` and produce a low-confidence screen.
- ENCORE can flag which activities deserve spatial attention, but ENCORE is not site-specific and cannot prove a sensitive location.

## Questions

Ask up to 5:

1. What sites/assets should we include?
2. What type is each site: factory, office, warehouse, farm, mine, power plant, store, project site?
3. City/address/coordinates for each?
4. Is each site near rivers, lakes, wetlands, forests, farmland, coast, protected areas, or residential areas?
5. Does the site use water, land, discharge wastewater, emit pollution, or generate waste?

## Required Deliverable

```markdown
## Partner Brief
合伙人，先给结论：当前 Locate 是 {L0/L1/L2/L3} 数据等级，能做 {city/site/location}-level 初筛。

## Locate Draft Deliverable
| 地点/资产 | 类型 | 地址/城市 | 数据精度 | 自然接触点 | 初步敏感性 | 缺口 |
|---|---|---|---|---|---|---|

## Priority Location Screen
| 地点/资产 | 水相关 | 土地相关 | 生物多样性相关 | IBAT/空间证据状态 | 社区/监管敏感 | 初步优先级 |
|---|---|---|---|---|---|---|

## ENCORE / IBAT Evidence Note
| Tool | Used in Locate? | Evidence | Limitation |
|---|---|---|---|
| ENCORE | supporting only | activity nature-interface hypothesis | not location-specific |
| IBAT / WDPA / WDKBA / IUCN | primary if available | coordinates/boundary + licensed or public spatial source | no site claim without evidence |

## Evidence Gaps
| Gap | Why it matters | Next evidence |
|---|---|---|

## Partner Challenge Checklist
| Check | Pass? | Note |
|---|---|---|
```
