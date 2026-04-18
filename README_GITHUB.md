# TNFD Disclosure Skill · 自然相关财务披露专业助手

> 🌏 基于 TNFD v1.0 官方框架 + 四大 ESG 咨询方法论 + 中国本土标准  
> 📊 内置 ENCORE 数据（2025 年 9 月版）+ 416+ 家 TNFD 采纳者报告库  
> 🔍 支持对标分析 + LEAP 评估 + 审计检查全流程

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TNFD Version](https://img.shields.io/badge/TNFD-v1.0-blue)](https://tnfd.global)
[![ENCORE Version](https://img.shields.io/badge/ENCORE-2025.09-green)](https://encorenature.org)

---

**Hermes Agent / Claude Code Skill** — 专为 ESG 从业者、咨询顾问、企业可持续发展团队设计。

## 核心功能

- ✅ **对标分析（Phase 0）** — 匹配行业标杆（隆基/牧原/汇丰等），提取最佳实践
- ✅ **LEAP 评估（Phase 1）** — Locate → Evaluate → Assess → Prepare 全流程引导
- ✅ **审计检查（Phase 2）** — 14 项披露覆盖检查 + 模拟审计意见
- ✅ **数据内置** — ENCORE 行业依赖/影响矩阵 + TNFD 官方报告库链接
- ✅ **四大方法论** — 安永/德勤/普华永道/毕马威 TNFD 咨询框架对标
- ✅ **中国本土化** — CASS-ESG 6.0 + 证监会《上市公司可持续发展报告指引》

## 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/QUEQUEYNH36/tnfd-disclosure-skill.git
cd tnfd-disclosure-skill

# 初始化数据
python3 scripts/process_encore_data.py

# 符号链接到 Hermes
ln -s $(pwd) ~/.Hermes/skills/tnfd-disclosure
```

### 使用

```
用户：光伏行业有哪些公司披露了 TNFD？

Skill: 
光伏行业已披露 TNFD 的标杆企业：
- 隆基绿能（独立 TNFD 报告，2025 年 11 月）
- 协鑫科技（ESG 整合，2025 年 4 月）
- Vestas（独立 TNFD 报告，2024 年 12 月）

需要我帮您获取报告 PDF 或进入 LEAP 评估吗？
```

## 目录结构

```
tnfd-disclosure-skill/
├── SKILL.md                    # 主技能文件
├── README.md                   # 本文件
├── prompts/                    # Prompt 模板
│   ├── 00-benchmark.md         # 对标分析
│   ├── 01-locate.md            # Locate 阶段
│   ├── 02-evaluate.md          # Evaluate 阶段
│   ├── 03-assess.md            # Assess 阶段
│   ├── 04-prepare.md           # Prepare 阶段
│   └── 05-assurance.md         # Assurance 阶段
├── references/                 # 参考文档
│   ├── tnfd-benchmark-database.md
│   ├── tnfd-report-links.md
│   ├── longi-tnfd-case-study.md
│   ├── muyuan-tnfd-case-study.md
│   └── ...
├── data/                       # 数据文件
│   ├── encore_raw/             # ENCORE 原始 CSV（需自行下载）
│   ├── encore_processed/       # ENCORE 处理后 JSON
│   └── tnfd_report_links.json  # 报告链接清单
├── scripts/
│   └── process_encore_data.py  # ENCORE 数据处理脚本
└── .gitignore
```

## 数据来源

| 数据 | 来源 | 许可 |
|------|------|------|
| ENCORE 数据 | https://encorenature.org | CC BY-SA 4.0 |
| TNFD 报告库 | https://tnfd.global/knowledge-hub/example-tnfd-reporting/ | 公开信息 |
| TNFD 框架 | https://tnfd.global/recommendations/ | 公开信息 |

## 参考文档

- [TNFD 官方](https://tnfd.global)
- [ENCORE 数据库](https://encorenature.org)
- [自然资本议定书](https://capitalscoalition.org/capitals-approach/natural-capital-protocol/)

## 许可证

MIT License — 详见 [LICENSE](LICENSE) 文件

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

- GitHub Issues: https://github.com/QUEQUEYNH36/tnfd-disclosure-skill/issues
- Email: [你的邮箱]

---

**Made with ❤️ for ESG professionals**
