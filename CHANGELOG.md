# TNFD-disclosure 更新日志

所有重要的更新都会记录在此文件中。遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 规范。

---

## [Unreleased]

### 优化

- **README 全面重构**：解决定位模糊、快速开始残缺、语言混乱问题
- **新增"What is this?"模块**：明确 Skill = AI Agent Prompt Library，不是 Python CLI
- **新增三框架适配说明**：Hermes / Claude Code / OpenClaw 安装方式
- **新增 A 阶段量化成熟度表**：Skill 能力边界透明化
- **新增官方参考文献列表**：Big 4 方法论标注待核验，附官方 PDF 链接
- **新增中国本土化独立章节**：区分《可持续发展报告指引》≠ TNFD
- **新增数据源说明表**：免费/付费/用途/LEAP 阶段全部对齐
- **修复 ASCII 方框表格**：全面改用 Markdown 原生表格

### ⚠️ P0 信息准确性修正（Web 验证）

- **修正**：ENCORE "完全免费" → 基础免费/高级付费（来源：encorenature.org 2026-04）
- **新增**：IBAT 数据源说明 — 商业订阅，Research 有免费额度（来源：ibat-alliance.org 2026-04）
- **修正**：中国强制披露（可持续发展指引）≠ TNFD
- **删除**：L1-L4 非官方子阶段编号（标注为"基于官方框架的自定义拆解"）
- **标注**：Big 4 方法论标记为"⚠️ 待核验"

### 🆕 PRD v2.0 架构重构

- **新增**：Definition Engine（TNFD vs TCFD 核心区别 — 来源验证）
- **新增**：LEAP 交付物指南（Input + Deliverable 格式）
- **新增**：A 阶段量化成熟度（L1-L4 分层）
- **新增**：S3 顾问高压对话协议（溯源免死、禁止废话、防御性交付）
- **新增**：数据源 × LEAP 阶段映射表（Web 验证版）
- **修正**：中国政策现状（可持续发展报告指引 ≠ TNFD）

### 🆕 官方数据源清单

- TNFD v1.0 中文 PDF（含下载链接）
- ENCORE：Biodiversity Module（2025年新增）
- IBAT：三大数据集（WDPA 303,313个保护区 / IUCN 166,045物种 / KBA 16,495个）
- 验证状态标注 · 开发中

### 计划中

- \[ \] 支持更多行业（金融、矿业、房地产等）
- \[ \] ENCORE 数据自动更新机制
- \[ \] 英文版 Skill 和文档
- \[ \] 与 TNFD 官方 API 对接
- \[ \] 支持 CSV/Excel 批量导入

---

## [2.0.0] · 2026-04-19 · v2 重大更新：PUA 行为控制系统

### 新增

**/tnfd 指令系统**
- 13 条指令：/tnfd new/status/kpi/benchmark/locate/evaluate/assess/prepare/audit/report/save/reset
- LEAP 流程全覆盖（Phase 0-5）
- 状态持久化（~/.tnfd/project-state.json）
- Sprint Banner + KPI 卡格式化输出

**TNFD PUA Handler**
- scripts/tnfd_handler.py — 状态管理 + Banner 输出 + KPI 卡
- ~/.tnfd/config.json — 用户配置
- ~/.tnfd/commands.json — 指令定义
- ~/.tnfd/project-state.json — 项目状态

**PUA 行为控制**
- Sprint Banner：Unicode 方框进度条
- KPI 卡：绩效报告卡
- 主动触发：阶段完成/风险发现/数据质量问题提醒
- 失败升级：L1-L4 压力升级

### 优化

- SKILL.md 全面重构，整合 PUA 指令系统
- README.md 新增 /tnfd 指令系统说明
- 安装流程更新（新增 Handler 安装步骤）

---

## [1.0.0] · 2026-04-19 · V1 首发

### 新增

**核心功能**
- Phase 0: Benchmark Analysis（对标分析）
  - 416+ 家 TNFD 采纳者报告库
  - 行业标杆匹配（光伏/养殖/金融/矿业等）
  - 最佳实践提取和差距分析框架
  - 直接发送报告 PDF 链接功能

- Phase 1: LEAP Assessment（LEAP 评估）
  - Locate（定位）：资产坐标 + 空间风险分析
  - Evaluate（评价）：ENCORE 数据集成（2025 年 9 月版）
  - Assess（评估）：风险量化 + 机遇识别 + 供应链风险模型
  - Prepare（准备）：TNFD 报告模板 + 响应策略

- Phase 2: Assurance（审计检查）
  - 14 项 TNFD 披露建议覆盖检查
  - 数据质量验证清单
  - 模拟审计意见输出

**数据文件**
- `data/tnfd_report_links.json` — TNFD 报告链接 JSON（416+ 条）
- `data/encore_processed/` — ENCORE 处理后数据
  - `ecosystem_services.json` — 48 个生态系统服务
  - `dependency_by_industry.json` — 21 个行业依赖矩阵
  - `pressure_by_industry.json` — 21 个行业影响矩阵
  - `industry_summary.json` — 行业摘要

** Prompt 模板**
- `prompts/00-benchmark.md` — 对标分析 Prompt
- `prompts/01-locate.md` — Locate 阶段 Prompt
- `prompts/02-evaluate.md` — Evaluate 阶段 Prompt
- `prompts/03-assess.md` — Assess 阶段 Prompt
- `prompts/04-prepare.md` — Prepare 阶段 Prompt
- `prompts/05-assurance.md` — Assurance 阶段 Prompt

**参考文档**
- `references/tnfd-benchmark-database.md` — 行业标杆数据库
- `references/tnfd-report-links.md` — 报告链接清单
- `references/tnfd-leap-complete-guide.md` — LEAP 完整指南
- `references/natural-capital-protocol-guide.md` — 自然资本议定书
- `references/big4-methodologies.md` — 四大方法论对照
- `references/industry-guidance.md` — 行业指南汇总
- `references/tnfd-sector-guidance-complete.md` — 17 行业指南
- `references/longi-tnfd-case-study.md` — 隆基案例研究
- `references/longi-muyuan-tnfd-comparison.md` — 隆基 vs 牧原对比
- `references/china-esg-standards.md` — 中国 ESG 标准体系
- `references/ey-gds-level-protocol.md` — EY 职级对标协议
- `references/partner-warm-pua-protocol.md` — 合伙人温情式 PUA

**脚本**
- `scripts/process_encore_data.py` — ENCORE 数据处理脚本

### 文档

- `README.md` — 完整中文文档（TNFD 前世今生、项目愿景、使用指南）
- `QUICK_REFERENCE.md` — Agent 快速参考卡
- `SKILL.md` — Skill 主文件（面向 Agent 设计）
- `CHANGELOG.md` — 本更新日志

### 行业标杆

| 行业 | 标杆企业 | 报告类型 | 方法论 |
|------|---------|---------|--------|
| 光伏 | 隆基绿能 | 独立 TNFD 报告 | TNFD LEAP + 安永 CCaSS |
| 养殖 | 牧原股份 | ESG 整合披露 | TNFD LEAP + 德勤 + 自然资本议定书 |
| 金融 | 汇丰/渣打 | TNFD 试点报告 | TNFD LEAP |
| 矿业 | 力拓 | 独立 TNFD 报告 | TNFD LEAP + ICMM |

### 方法论覆盖

- TNFD v1.0 14 项披露建议
- 自然资本议定书 9 步骤（Capitals Coalition）
- 四大 ESG 方法论（EY/Deloitte/PwC/KPMG）
- 中国本土标准（CASS-ESG 6.0、证监会指引）

---

## 安装

```bash
# 克隆仓库
git clone https://github.com/newversionparty-cn/TNFD-disclosure.git
cd TNFD-disclosure

# 初始化数据（首次使用需要）
python3 scripts/process_encore_data.py

# 符号链接到 Hermes
ln -s $(pwd) ~/.Hermes/skills/tnfd-disclosure
```

---

## 如何参与

Issues 和 Pull Request 欢迎！请查看 [GitHub Issues](https://github.com/newversionparty-cn/TNFD-disclosure/issues)。

