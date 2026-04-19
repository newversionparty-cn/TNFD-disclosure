# TNFD-disclosure

> 🌍 让自然相关财务信息披露与 TCFD 一样触手可及。| [English Version](./README_en.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TNFD 版本](https://img.shields.io/badge/TNFD-v1.0-blue)](https://tnfd.global)
[![ENCORE 版本](https://img.shields.io/badge/ENCORE-2025.09-green)](https://encorenature.org)
[![支持平台](https://img.shields.io/badge/Platform-Hermes%7CClaude%20Code%7COpenClaw-blueviolet)](https://github.com/newversionparty-cn/TNFD-disclosure)
[![状态](https://img.shields.io/badge/Status-活跃-brightgreen)]()

---

## 这是什么？

**TNFD-disclosure 是一个 AI Agent Skill（提示词库），不是 Python CLI 工具，也不是 Web 应用。**

它是一套结构化的提示词 + 知识库，专为支持自定义 Skill 的 AI Agent 设计——目前支持 Hermes、Claude Code 和 OpenClaw。

| 如果你是... | 使用方式 |
|-------------|---------|
| **ESG 顾问** | 将 `SKILL.md` 内容作为 AI Agent 的 System Prompt 使用 |
| **开发者** | 参考 `prompts/` 目录的模块化提示词模板，集成到你的 Agent |
| **AI Agent 用户** | 在支持 Skill 的 Agent 中安装此包，喊 `/tnfd` 激活 |

---

## 架构

```
TNFD-disclosure/
├── SKILL.md              # 主 Skill 文件（System Prompt + 知识库）
├── QUICK_REFERENCE.md    # Agent 快速参考卡
├── prompts/              # 模块化提示词模板
│   ├── 00-benchmark.md    # 阶段 0：标杆对标
│   ├── 01-locate.md      # 阶段 1：定位（Locate）
│   ├── 02-evaluate.md    # 阶段 2：评价（Evaluate）
│   ├── 03-assess.md       # 阶段 3：评估（Assess）
│   ├── 04-prepare.md      # 阶段 4：准备（Prepare）
│   └── 05-assurance.md    # 阶段 5：审计（Assurance）
├── references/            # 参考文档知识库
│   ├── tnfd-leap-complete-guide.md
│   ├── big4-methodologies.md
│   ├── china-esg-standards.md
│   └── ...
├── data/                 # 内置数据
│   ├── encore_processed/ # ENCORE 处理后 JSON（2025年9月版）
│   └── tnfd_report_links.json
└── scripts/
    ├── tnfd_handler.py   # 状态管理器（可选）
    └── process_encore_data.py
```

### 工作流

```
阶段 0          阶段 1：LEAP                    阶段 2
  │             ┌──┬───┬────┬────┐               │
  ▼             │L │ E │  A │  P │               ▼
标杆对标  ──►  └──┴───┴────┴────┘  ─────────►  审计检查
  │             （定位→评价→评估→准备）            │
  ▼                                                ▼
标杆案例      ───────────────────────────────►  报告生成
```

---

## 快速开始

### 步骤 1：安装 Skill

**Hermes（推荐）**
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

### 步骤 2：激活 Skill

在任何支持 Skill 的 Agent 对话中输入：
```
/tnfd
```

Agent 将显示 Sprint Banner 并进入 TNFD 工作流程。

### 步骤 3：开始项目

```
/tnfd new                           # 新建项目
/tnfd benchmark                     # 阶段 0：标杆对标
/tnfd locate                       # 阶段 1：定位
/tnfd evaluate                      # 阶段 2：评价
/tnfd assess                        # 阶段 3：评估
/tnfd prepare                       # 阶段 4：准备
/tnfd audit                         # 阶段 5：审计
/tnfd report                        # 生成报告
```

---

## TNFD LEAP 框架

TNFD v1.0（2023年9月发布）的核心是 **LEAP 方法论**：

| 阶段 | 英文 | 核心问题 | 主要数据源 |
|------|------|---------|-----------|
| **L** | Locate（定位） | 你的资产在哪里？这些地方生态敏感吗？ | WDPA、IBAT、WRI Aqueduct、生态红线 |
| **E** | Evaluate（评价） | 你的业务依赖哪些自然资本？影响是什么？ | **ENCORE**（核心必用） |
| **A** | Assess（评估） | 这些依赖/影响，能转成财务数字吗？ | NGFS 框架 + 替代成本法 |
| **P** | Prepare（准备） | 如何披露？符合 TNFD 14 项建议吗？ | TNFD v1.0 披露模板 |

### A 阶段量化成熟度

| 成熟度 | 能做到 | Skill 能指导 |
|--------|--------|-------------|
| L1（基础） | 定性风险识别 | ✅ 可以 |
| L2（进阶） | 半定量（面积、体积） | ✅ 可以 |
| L3（高级） | 财务等效量化 | ⚠️ 给方法论，不给精确数字 |
| L4（精确） | 需要客户 ERP 数据 | ❌ Skill 无法替代 |

> ⚠️ **Skill 的边界**：Skill 是"导航仪"，不是"替代者"。精确财务量化需要客户内部数据，Agent 无法替代。

---

## 数据源说明

| 数据源 | 用途 | LEAP 阶段 | 免费？ | 备注 |
|--------|------|-----------|--------|------|
| **ENCORE** | 依赖度/影响度矩阵 | E, A | 基础版免费 | [官网](https://encorenature.org) |
| **WDPA** | 保护区数据库 | L | 免费 | UNEP-WCMC |
| **IBAT** | 综合生物多样性 | L, E | 研究用途免费 | 商业需订阅 |
| **WRI Aqueduct** | 水风险地图 | L, A | 免费 | [官网](https://www.wri.org/aqueduct) |
| **生态红线** | 中国生态敏感区 | L | 非公开 | 需从自然资源部获取 |
| **蔚蓝地图** | 企业污染记录 | L, E | 部分免费 | [IPE](https://www.ipe.org.cn) |

---

## 中国本土化

**中国 TNFD 现状**：
- 证监会 2024 年发布《上市公司可持续发展报告指引》——**不等同于 TNFD**
- 2026 年 A+H 股强制的是这个指引，不是 TNFD 本身
- TNFD 在中国仍处于**自愿采纳**阶段
- 头部企业采纳：隆基绿能（2025.11）、牧原股份（2026.3）

**本土标准参考**：
- CASS-ESG 6.0（中欧对接版）
- 证监会《上市公司可持续发展报告指引》（2024）
- 生态环境部《企业环境信息依法披露管理办法》

---

## 核心功能

### 阶段 0：标杆对标

输入行业名称 → 匹配标杆案例（隆基/牧原/汇丰/力拓）→ 输出差距分析框架

### 阶段 1–4：LEAP 评估

- **L – 定位**：资产坐标 → 生态敏感区叠加分析
- **E – 评价**：行业分类 → ENCORE 依赖/影响矩阵
- **A – 评估**：风险量化 + 机遇识别
- **P – 准备**：TNFD 报告编制

### 阶段 5：审计检查

14 项 TNFD 披露建议覆盖检查（治理 2 项 + 战略 2 项 + 风险与影响管理 4 项 + 指标与目标 6 项）

---

## 行业标杆案例

### 隆基绿能（光伏行业）

**报告信息**：
- 发布时间：2025 年 11 月（COP30）
- 报告类型：独立 TNFD 报告
- 方法论：TNFD LEAP + 安永 CCaSS

**核心亮点**：
- 🏆 中国光伏企业首份独立 TNFD 报告
- 💰 自然资本评估试点（嘉兴基地节约 2149.6 万元）
- 🎯 2050 年生物多样性"净零损失"目标
- 🌿 2060 年自然"净正面影响"远景

| 指标 | 数据 |
|------|------|
| LEAP 完整度 | 4/4 阶段完整 |
| 14 项覆盖率 | 10/14 项（71%） |

### 牧原股份（养殖行业）

**报告信息**：
- 发布时间：2026 年 3 月（HKEX）
- 方法论：TNFD LEAP + 德勤 + 自然资本议定书

**监测体系**：

| 类别 | 指标数 | 频次 |
|------|--------|------|
| 土壤 | 16 项 | 2次/年 × 100%覆盖 |
| 地下水 | 12 项 | 2次/年 × 100%覆盖 |
| 地表水 | 6 项 | 1-4次/年 |
| 农产品 | 15 项 | 1-2次/年 |

---

## 方法论框架

### 四大咨询机构 TNFD 方法论

| 机构 | 方法论名称 | 核心关键词 |
|------|-----------|-----------|
| **安永 (EY)** | CCaSS | 自然资本货币化 / 财务整合 / IUCN 合作 |
| **德勤 (Deloitte)** | Climate & Sustainability | 数字化监控 / 循环经济 / 自然资本议定书 |
| **普华永道 (PwC)** | Five Things | 5步框架 / 检查清单 / 披露模板 |
| **毕马威 (KPMG)** | NATURE Framework | 成熟度评估 / 分阶段实施 / 路线图规划 |

> ⚠️ 以上 Big 4 方法论引用基于公开资料，详情请参阅各公司官方 TNFD 白皮书。**来源验证状态：⚠️ 待核验。**

### 官方参考文献

| 文献 | 来源 | 链接 |
|------|------|------|
| TNFD v1.0 建议（官方） | TNFD | [PDF](https://tnfd.global/wp-content/uploads/2023/08/Recommendations-of-the-Taskforce-on-Nature-related-Financial-Disclosures.pdf) |
| TNFD LEAP 完整指南 | TNFD | [链接](https://tnfd.global/publication/additional-guidance-on-assessment-of-nature-related-issues-the-leap-approach/) |
| ENCORE 数据库 | UNEP FI + Global Canopy | [链接](https://encorenature.org) |
| IBAT 综合生物多样性工具 | BirdLife/IUCN/Conservation International/UNEP-WCMC | [链接](https://www.ibat-alliance.org) |
| WRI Aqueduct 水风险地图 | 世界资源研究所 | [链接](https://www.wri.org/aqueduct) |
| NGFS 自然风险概念框架 | 央行与监管机构绿色金融网络 | [链接](https://www.ngfs.fr) |

---

## 数据结构

```
TNFD-disclosure/
├── SKILL.md                    # 主 Skill 文件
├── QUICK_REFERENCE.md          # Agent 快速参考
├── CHANGELOG.md                # 版本记录
├── prompts/                    # 模块化提示词
│   ├── 00-benchmark.md         # 标杆对标
│   ├── 01-locate.md           # Locate 阶段
│   ├── 02-evaluate.md         # Evaluate 阶段
│   ├── 03-assess.md           # Assess 阶段
│   ├── 04-prepare.md          # Prepare 阶段
│   └── 05-assurance.md         # Assurance 阶段
├── references/                 # 知识库
│   ├── tnfd-leap-complete-guide.md
│   ├── big4-methodologies.md
│   ├── china-esg-standards.md
│   └── ...
├── data/                       # 内置数据
│   ├── encore_processed/       # ENCORE JSON
│   └── tnfd_report_links.json
└── scripts/
    └── process_encore_data.py
```

---

## 贡献指南

欢迎提交 Issue 和 Pull Request！

**提交前检查**：
- [ ] 方法论引用已标注来源
- [ ] 数据源已注明免费/付费
- [ ] 没有凭记忆编造的统计数据
- [ ] 新的提示词经过测试

---

## 许可证

MIT License — 详见 [LICENSE](LICENSE)

---

## 附录：中国 vs 国际 TNFD 现状对比

| 维度 | 中国 | 国际 |
|------|------|------|
| **监管要求** | 自愿（指引≠TNFD） | G20 推动，ISSB 参考 |
| **采纳企业** | 头部试点（隆基、牧原） | 416+ 机构（截至 2025.12） |
| **数据环境** | 生态红线不对外公开 | WDPA/IBAT 免费/订阅 |
| **方法论** | CASS-ESG 6.0 对接 | ENCORE + LEAP |
| **审计要求** | 无强制第三方鉴证 | TNFD 提供鉴证指南 |

> 📊 数据来源：TNFD 官方（tnfd.global）、IPE（蔚蓝地图）、证监会官网（csrc.gov.cn）

---

*最后更新：2026-04-20*
