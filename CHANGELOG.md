# TNFD-disclosure 更新日志

所有重要的更新都会记录在此文件中。遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 规范。

---

## \[Unreleased\] · 开发中

### 计划中

- \[ \] 支持更多行业（金融、矿业、房地产等）
- \[ \] ENCORE 数据自动更新机制
- \[ \] 英文版 Skill 和文档
- \[ \] 与 TNFD 官方 API 对接
- \[ \] 支持 CSV/Excel 批量导入

---

## \[1.0.0\] · 2026-04-19 · V1 首发

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

