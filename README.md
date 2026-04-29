# TNFD-disclosure · 自然相关财务披露助手

> 🌍 让自然相关财务信息披露与 TCFD 一样触手可及。
> 基于 TNFD v1.0 官方框架 + 四大 ESG 咨询方法论 + 中国本土标准。
> 内置 ENCORE 数据 + 提供 TNFD 官方报告库入口 + 精选行业案例索引。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TNFD Version](https://img.shields.io/badge/TNFD-v1.0-blue)](https://tnfd.global)
[![ENCORE Version](https://img.shields.io/badge/ENCORE-2025.09-green)](https://encorenature.org)
[![Platform](https://img.shields.io/badge/Platform-Hermes%20%7C%20Claude%20Code%20%7C%20OpenClaw-purple)](https://github.com/newversionparty-cn/TNFD-disclosure)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

[**English Version**](README_en.md) · [**快速开始**](#快速开始) · [**方法论**](#方法论框架) · [**案例**](#行业标杆案例)

---

## TNFD Framework Overview

![TNFD v1.0 Framework — LEAP + 14 Disclosure Recommendations](assets/tnfd-framework-infographic.png)

---

## 这是什么？

**TNFD-disclosure 是一个 AI Agent Skill（提示词库），不是 Python CLI 工具，也不是 Web 应用。**

它是一套结构化的提示词 + 知识库，专为支持自定义 Skill 的 AI Agent 设计——目前支持 **Hermes**、**Claude Code** 和 **OpenClaw**。

| 如果你是... | 使用方式 |
|-------------|---------|
| ESG 顾问 | 将 `SKILL.md` 内容作为 AI Agent 的 System Prompt |
| 企业可持续发展团队 | 启动 Agent 直接执行 TNFD LEAP 评估 |
| AI Agent 开发者 | 集成 Skill 到你的 Agent 框架 |
| 学术研究者 | 参考方法论框架 + 内置文献数据 |

---

## 核心功能

### 三阶段工作流程

```
Phase 0: 对标分析     →     Phase 1: LEAP 评估     →     Phase 2: 审计检查
  (Benchmark)                (Assess)                       (Assurance)
```

- **Phase 0 — Benchmark Analysis**：匹配行业标杆企业，分析最佳实践与差距
- **Phase 1 — LEAP Assessment**：Locate → Evaluate → Assess → Prepare 四阶段评估
- **Phase 2 — Assurance**：14 项披露建议覆盖检查，模拟审计意见

### LEAP 四阶段

| 阶段 | 核心问题 | 输出物 | 预计时间 |
|------|---------|--------|---------|
| **L**ocate · 定位 | 资产/供应链在哪里？ | 资产坐标清单 + 空间风险地图 | 1-2 周 |
| **E**valuate · 评价 | 依赖和影响是什么？ | 行业依赖矩阵 + 影响驱动因素 | 1-2 周 |
| **A**ssess · 评估 | 财务风险/机遇？ | 风险量化分析 + 机遇清单 | 2-4 周 |
| **P**repare · 准备 | 如何披露/响应？ | TNFD 报告 + 响应策略 | 2-4 周 |

### TNFD 14 项披露建议

| 支柱 | 建议数 | 核心检查点 |
|------|--------|-----------|
| **治理** Governance | 3 项 | 董事会监督 · 管理层角色 · 人权与利益相关方 |
| **战略** Strategy | 4 项 | 依赖与影响识别 · 业务模式影响 · 战略韧性 · 优先位置 |
| **风险与影响管理** Risk & Impact | 4 项 | 直接运营识别评估 · 价值链识别评估 · 监控流程 · ERM 整合 |
| **指标与目标** Metrics & Targets | 3 项 | 风险与机遇指标 · 依赖与影响指标 · 目标与绩效 |

---

## 为什么做这个项目

### 痛点

- **信息分散**：TNFD 官方文档 100+ 页，ENCORE 数据 18 个 CSV，行业指南分布在多个网站
- **咨询成本高**：外部 TNFD 咨询通常需要显著预算；具体金额需按项目范围和服务商报价核验
- **工具缺失**：缺乏一站式评估工具，数据收集和处理耗时

### 核心价值

| 维度 | 传统方式 | TNFD-disclosure |
|------|---------|----------------|
| 时间成本 | 8-12 周 | 2-4 周 |
| 经济成本 | 需按项目报价核验 | 免费开源 |
| 专业门槛 | 需要四大咨询 | AI 辅助引导 |
| 数据获取 | 手动收集 | 内置 ENCORE |
| 行业对标 | 付费购买 | 精选案例索引 |
| 审计准备 | 额外收费 | 内置检查 |

---

## 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/newversionparty-cn/TNFD-disclosure.git
cd TNFD-disclosure

# 符号链接到 Hermes
ln -s $(pwd) ~/.Hermes/skills/tnfd-disclosure
```

### 使用示例

**场景 1：行业对标**

```
用户：光伏行业有哪些公司披露了 TNFD？

TNFD-disclosure：光伏行业已披露 TNFD 的标杆企业：

| 公司 | 报告类型 | 发布时间 | 方法论 | 亮点 |
|------|---------|---------|--------|------|
| 隆基绿能 | 待核验 | 待核验 | 待核验 | 本地 claim registry 有待核验线索 |
| 协鑫科技 | 待核验 | 待核验 | 待核验 | 需官方报告和页码支持 |
| Vestas | 待核验 | 待核验 | 待核验 | 本地 claim registry 有待核验线索 |

需要我帮您获取报告 PDF 或进入 LEAP 评估吗？
```

**场景 2：启动 LEAP 评估**

```
用户：我想做 TNFD 披露，怎么开始？

TNFD-disclosure：推荐流程：
Phase 0: 对标分析（了解行业最佳实践）
Phase 1: LEAP 评估（Locate → Evaluate → Assess → Prepare）
Phase 2: 审计检查（14 项覆盖检查）

请选择您的起点。
```

---

## 方法论框架

### 四大方法论对比

| | 安永 (EY，待核验) | 德勤 (Deloitte，待核验) | 普华永道 (PwC，待核验) | 毕马威 (KPMG，待核验) |
|---|---|---|---|---|
| **方法论** | 待核验公开资料 | 待核验公开资料 | 待核验公开资料 | 待核验公开资料 |
| **特色** | 待核验 | 待核验 | 待核验 | 待核验 |
| **合作** | 待核验 | 待核验 | 待核验 | 待核验 |

### TNFD 与 TCFD 的关系

TNFD 在 TCFD 四大支柱基础上，新增 **LEAP 评估方法** 和 **自然影响管理** 维度：

- **治理** → 对应 TCFD 治理
- **战略** → 对应 TCFD 战略
- **风险与影响管理** → 扩展自 TCFD 风险管理，新增自然影响管理
- **指标与目标** → 扩展自 TCFD 指标与目标，新增自然定价相关指标

---

## 行业标杆案例

### 隆基绿能（光伏行业，待核验案例线索）

> **事实状态**：以下内容必须先在 `data/case_claims_verification.json` 中补充来源 URL 和报告页码，方可作为确定事实使用。

**待核验方向**：
- 是否发布独立 TNFD 或自然相关披露
- 是否采用 LEAP
- 是否包含自然资本评估、目标设定和第三方合作
- 14 项披露覆盖率和任何金额型指标

---

### 牧原股份（养殖行业，待核验案例线索）

> **事实状态**：以下内容必须先在 `data/case_claims_verification.json` 中补充来源 URL 和报告页码，方可作为确定事实使用。

**待核验方向**：
- 是否发布 TNFD 相关披露
- 是否采用 LEAP 或自然资本议定书
- 监测指标数量、供应链模型、情景分析等具体说法

---

## 数据结构

```
TNFD-disclosure/
├── SKILL.md              # Agent Skill 定义（System Prompt）
├── QUICK_REFERENCE.md    # 快速参考卡片
├── CHANGELOG.md          # 更新日志
├── assets/               # 静态资源
│   └── *.png             # 信息图、流程图
├── data/                 # 内置数据
│   └── encore/           # ENCORE 解析数据
├── prompts/              # LEAP 各阶段 Prompt
│   ├── 01-locate.md
│   ├── 02-evaluate.md
│   ├── 03-assess.md
│   └── 04-prepare.md
├── references/           # 方法论文档
│   ├── tnfd-leap-complete-guide.md
│   ├── data-sources-registration-guide.md
│   ├── industry-guidance.md
│   ├── big4-methodologies.md
│   └── china-esg-standards.md
└── scripts/              # 辅助脚本
    └── process_encore_data.py
```

---

## 贡献指南

欢迎提交 Issue 和 Pull Request！

### 报告质量评级标准（自评参考）

| 等级 | 描述 | 14 项覆盖 |
|------|------|---------|
| A | 鉴证准备度高，证据链较完整 | 14/14 或有充分解释 |
| B+ | 基本完整，有少量改进空间 | 12-13/14 |
| B | 部分披露，存在重要整改项 | 10-11/14 |
| C | 初步尝试，需要重大改进 | 7-9/14 |
| D | 框架搭建阶段 | < 7/14 |

---

## 免责声明

本 Skill 基于 TNFD v1.0 官方框架和四大公开方法论提供指导，**不构成正式审计或鉴证意见**。正式披露建议：
1. 完成完整的 LEAP 评估
2. 进行第三方验证
3. 咨询专业审计机构

---

*项目维护者：[Tom](https://github.com/newversionparty-cn) · 提交 Issue 或 PR 让我们做得更好*
