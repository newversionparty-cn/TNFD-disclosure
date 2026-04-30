# TNFD-disclosure · 自然相关财务披露工作台

> 为 ESG 顾问、企业可持续发展团队和 AI Agent 提供可追溯、可验证、可阶段性交付的 TNFD 披露工作流。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TNFD v1.0](https://img.shields.io/badge/TNFD-v1.0-blue)](https://tnfd.global)
[![ENCORE 2025.09](https://img.shields.io/badge/ENCORE-2025.09-green)](https://encorenature.org)
[![Validate](https://img.shields.io/badge/Claim%20Validation-10%2F10-brightgreen)](#事实治理)
[![Platform](https://img.shields.io/badge/Platform-Hermes%20%7C%20Claude%20Code%20%7C%20OpenClaw-purple)]()

[**English**](README_en.md) · [**快速开始**](#快速开始) · [**工作流**](#工作流) · [**文件结构**](#文件结构) · [**事实治理**](#事实治理)

---

## 解决的问题

| 痛点 | 现状 |
|---|---|
| TNFD 官方文档分散 | 本 Skill 整合 LEAP 组件、14 项建议、General Requirements、Metrics 架构 |
| 案例数字不可审计 | Claim Registry + validate_claims.py 强制 pending claims 不得作为确定事实输出 |
| 内部评分模型混淆为官方方法 | 所有自定义公式标注 `method_status: internal`，不用于外部披露 |
| Assurance 话术越界 | 输出"鉴证准备度评级"而非审计意见 |
| 中国监管与 TNFD 混为一谈 | 明确区分《指引》强制披露 vs TNFD 自愿对齐 |

---

## 小白 LEA 工作流

默认模式：用户是 Partner，Agent 是冲 Manager 的四大 Senior Consultant。压力作用于 Agent 自己的交付标准：必须结论先行、形成表格/矩阵/登记册、列明证据缺口，不允许只讲概念。

```
Intake → Locate → Evaluate → Assess → Export
 PwC lens  Deloitte lens  KPMG lens  EY lens  Deloitte/PwC lens
```

用户不懂 TNFD 也可以从 `/tnfd start` 开始，只提供公司、业务、行业、地点和目的，Agent 会先生成低数据版本 LEA 初筛。

## 完整工作流

```
Scope → Benchmark → Locate → Evaluate → Assess → Prepare → Assurance Readiness
  C1-C4    L1-L4      E1-E4    A1-A4    P1-P4
```

每个阶段前检查 evidence gate，证据不足时输出 gap，不生成"完整报告"。

### 命令

| 命令 | 功能 | Evidence Gate |
|---|---|---|
| `/tnfd` | 启动助手 | 无 |
| `/tnfd start` | 启动小白 LEA 向导 | 无 |
| `/tnfd new` | 新建小白 LEA 项目 | 公司名 + 行业 |
| `/tnfd intake` | 项目 Intake 问卷 | 公司、业务、行业、地点、目的 |
| `/tnfd status` | 项目状态 | 项目状态文件 |
| `/tnfd benchmark` | 行业对标 | 无 |
| `/tnfd locate` | Locate（C1-C4 + L1-L4） | 资产坐标 + 供应链布局 |
| `/tnfd evaluate` | Evaluate（E1-E4） | ENCORE/BRF 筛选输出 |
| `/tnfd assess` | Assess（A1-A4） | LEAP 输出 + 财务数据 |
| `/tnfd prepare` | Prepare（P1-P4） | 14 项建议 + General Requirements 检查 |
| `/tnfd audit` | 鉴证准备度 | 所有阶段 evidence |
| `/tnfd export` | 导出 Excel/PDF 工作底稿 | 已保存 LEA 状态 |
| `/tnfd save` | 保存状态 | 无 |
| `/tnfd reset` | 重置项目 | 无 |

---

## 文件结构

```
TNFD-disclosure/
├── SKILL.md                        # Agent Skill 定义（154 行，符合 v4 规范）
├── prompts/                        # 分阶段提示词
│   ├── 00-benchmark.md             #   Phase 0：对标分析
│   ├── 00-novice-start.md          #   小白 LEA 启动
│   ├── 01-project-intake.md        #   项目 Intake
│   ├── 01-locate.md                #   Phase 1：定位
│   ├── 02-locate-wizard.md         #   小白 Locate 向导
│   ├── 02-evaluate.md              #   Phase 2：评价
│   ├── 03-evaluate-wizard.md       #   小白 Evaluate 向导
│   ├── 03-assess.md                #   Phase 3：评估
│   ├── 04-assess-wizard.md         #   小白 Assess 向导
│   ├── 04-prepare.md               #   Phase 4：准备披露
│   ├── 05-lea-summary.md           #   LEA 汇总
│   ├── 05-assurance.md             #   Phase 5：鉴证准备度
│   └── 06-export-artifacts.md      #   手动导出 Excel/PDF
├── references/
│   ├── beginner/                    # 小白模式 + Big4 PUA Senior Mode
│   ├── framework/                   # TNFD 官方框架参考
│   │   ├── leap-components.md       #   C1-C4 / L1-L4 / E1-E4 / A1-A4 / P1-P4
│   │   ├── recommendations-14.md   #   14 项建议 + evidence request
│   │   ├── general-requirements.md  #   6 项 General Requirements gate
│   │   ├── metrics-architecture.md   #   Core / Sector / Additional / Comply-or-explain
│   │   └── value-chains.md          #   上游/下游/traceability
│   ├── localization/
│   │   └── china-sustainability-reporting.md  # 中国监管判断 + TNFD 自愿对齐
│   ├── data-sources/
│   │   └── encore-ibat-leap-guide.md          # ENCORE / IBAT 在 LEAP 中的使用边界
│   └── sectors/
│       └── sector-guidance-index.json         # 行业指南状态索引
├── data/
│   ├── case_claims_verification.json  # Claim Registry（12 条 pending）
│   ├── nature_tools_leap_mapping.json # ENCORE / IBAT 结构化 LEAP 映射
│   ├── tnfd_report_links.json        # TNFD 官方报告库索引
│   ├── encore_raw/                    # ENCORE 原始数据（2025.09）
│   └── encore_processed/             # 解析后数据（48 个生态系统服务 × 21 个行业）
├── scripts/
│   ├── tnfd_handler.py               # /tnfd 命令处理器
│   ├── process_encore_data.py        # ENCORE 数据处理
│   ├── generate_lea_workbook.py      # Excel 工作底稿导出
│   ├── generate_lea_report.py        # DOCX/PDF/MD 报告导出
│   ├── validate_claims.py            # Claim 校验（CI ready）
│   └── smoke_test.sh                 # 冒烟测试（7/7 通过）
└── assets/
    └── tnfd-framework-infographic.png
```

---

## 事实治理

本 Skill 内所有案例引用受 Claim Registry 管理：

| 状态 | 含义 | 输出规则 |
|---|---|---|
| `verified` | Registry 有 source URL + 页码 | 可作为确定事实使用 |
| `pending` | Registry 有线索但未核验 | 只能表述为"待核验线索" |
| `rejected` | Registry 标记为不可用 | 禁止输出 |

当前 Registry 状态：**12 条 pending**，`validate_claims.py` 扫描活跃文件，确认 pending claim 不得被确定式输出。

运行 claim 校验：
```bash
python3 scripts/validate_claims.py
```

---

## 快速开始

**安装**

```bash
git clone https://github.com/newversionparty-cn/TNFD-disclosure.git
cd TNFD-disclosure

# 符号链接到 Hermes
ln -s $(pwd) ~/.Hermes/skills/tnfd-disclosure
```

**冒烟测试**

```bash
bash scripts/smoke_test.sh
```

**使用示例**

```
用户：我完全不懂 TNFD，怎么开始？

TNFD-disclosure：
• 合伙人，先给结论：你不需要先学完整 TNFD。我会带你完成 LEA 前三步。
• 先回答 5 个问题：公司、业务、行业、地点、目的。
• 我会输出低数据版本 Locate/Evaluate/Assess 工作底稿和证据缺口。

用户：/tnfd export

TNFD-disclosure：
• 导出只读取已保存 LEA 状态，不重新推断结论。
• 输出：TNFD_LEA_Workbook.xlsx + TNFD_LEA_Preliminary_Report.md/DOCX/PDF。
• 如 PDF 依赖不可用，保留 DOCX/MD fallback。
```

---

## 数据来源

| 来源 | 用途 | 状态 |
|---|---|---|
| [TNFD Recommendations v1.0](https://tnfd.global/recommendations/) | 框架基础 | ✅ 官方 |
| [TNFD LEAP v1.1](https://tnfd.global/leap/) | 官方组件定义 | ✅ 官方 |
| [ENCORE 2025.09](https://encorenature.org) | 依赖/影响路径底座 | ✅ 已集成 |
| [IBAT](https://www.ibat-alliance.org/data) | Locate 敏感地点、生物多样性筛查 | ⚠️ 需许可/用户报告 |
| [WWF BRF](https://riskfilter.org/biodiversity) | 行业权重调整 + Exposure | ✅ 已集成 |
| [TNFD Sector Guidance](https://tnfd.global/sector-guidance) | 行业追加指引 | ⚠️ 按索引核实 |
| 证监会《上市公司可持续发展报告指引》 | 中国监管判断 | ✅ 已集成 |
| CASS-ESG 6.0 | 中国本土标准 | ⚠️ 待官方核验 |

---

## 免责声明

本 Skill 提供方法论指导和工作流支持，**不构成正式审计或鉴证意见**。

- 不声称任何企业报告"完全符合 TNFD"
- 不出具审计意见、鉴证意见、"无保留意见"或"保留意见"
- 所有案例数字需附带来源和页码，或标注为待核验
- 自定义评分模型不得作为 TNFD 官方指标输出

正式披露建议完成 LEAP 评估并咨询专业机构。

---

## 联系方式

如有 TNFD 披露咨询需求，或希望参与本项目协作，欢迎扫码联系：

<div align="center">

![飞书二维码](./assets/contact-qr.png)

**扫码添加 · 备注"TNFD"**

</div>

---

*项目维护：[Tom](https://github.com/newversionparty-cn) · Issues & PR welcome*
