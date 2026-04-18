# TNFD Disclosure Skill · 自然相关财务披露专业助手

> 基于 TNFD v1.0 官方框架 + 四大 ESG 咨询方法论（Deloitte/PwC/EY/KPMG）+ 中国本土标准（CASS-ESG 6.0/证监会指引）

---

## 快速开始（3 分钟）

### Step 1: 安装 Skill

**Hermes Agent**：
```bash
# 符号链接到全局技能目录
ln -s ~/Desktop/TNFD/skill ~/.Hermes/skills/tnfd-disclosure
```

**Claude Code**：
```bash
# 复制 SKILL.md 到技能目录
cp ~/Desktop/TNFD/skill/SKILL.md ~/.claude/skills/
```

### Step 2: 初始化数据（首次使用）

```bash
cd ~/Desktop/TNFD/skill

# 1. 处理 ENCORE 数据（首次使用需要）
python3 scripts/process_encore_data.py

# 2. 验证数据
ls -la data/encore_processed/
```

**输出**：
- `ecosystem_services.json` — 48 个生态系统服务
- `dependency_by_industry.json` — 21 个行业依赖
- `pressure_by_industry.json` — 21 个行业影响
- `industry_summary.json` — 行业摘要

### Step 3: 激活 Skill

**触发词**（任一即可）：
- 「TNFD」
- 「自然相关财务披露」
- 「LEAP 框架」
- 「生物多样性风险」
- 「ENCORE 数据」
- 「ESG 披露」
- 「TNFD 报告」

### Step 3: 开始使用

**场景 1：学习 TNFD 知识**
```
用户：TNFD 是什么？

Skill: 欢迎使用 TNFD 披露专业助手。

在开始之前，我需要了解您的需求：
1. 您使用 TNFD Skill 的目的是什么？（学习/培训/披露/对标）
2. 您属于哪个行业？
3. 您之前是否了解过 TNFD？

根据您的回答，我将为您提供针对性的指导。
```

**场景 2：准备 TNFD 披露**
```
用户：我想做 TNFD 披露，我们是光伏行业。

Skill: 收到。光伏行业已披露 TNFD 的标杆企业：

| 公司 | 报告类型 | 发布时间 | 方法论 | 亮点 |
|------|---------|---------|--------|------|
| 隆基绿能 | 独立 TNFD 报告 | 2025 年 11 月 | TNFD LEAP + 安永 CCaSS | 自然资本评估试点 |
| 协鑫科技 | ESG 报告整合 | 2025 年 4 月 | TNFD LEAP | 供应链风险评估 |
| Vestas | 独立 TNFD 报告 | 2024 年 12 月 | TNFD LEAP | 有限鉴证 |

您想深入了解哪个标杆企业的实践？或者直接进入 LEAP 评估流程？
```

**场景 3：对标分析**
```
用户：想了解养殖行业的 TNFD 最佳实践。

Skill: 养殖行业已披露 TNFD 的标杆企业：

| 公司 | 报告类型 | 发布时间 | 方法论 | 亮点 |
|------|---------|---------|--------|------|
| 牧原股份 | ESG 报告整合 | 2026 年 3 月 | TNFD LEAP + 德勤 + 自然资本议定书 | 49 项监测指标 |
| Agrovision | Nature/TNFD 报告 | 2024 年 | TNFD LEAP | 秘鲁农业 |
| 新希望六和 | ESG 报告整合 | 2025 年 4 月 | TNFD 框架参考 | - |
| Bunge | Sustainability/ESG 报告 | 2024 年 | TNFD 框架参考 | 瑞士农业 |
| Charoen Pokphand Group | Nature/TNFD 报告 | 2024 年 | TNFD LEAP | 泰国正大集团 |

**牧原核心实践**：
1. 自然资本议定书应用：9 步骤完整
2. 监测体系：49 项指标（土壤 16 项、地下水 12 项...）
3. 监测频次：2 次/年，100% 覆盖
4. 供应链风险：风险传导模型 + 情景模拟

**更多报告**：[TNFD 官方报告库](https://tnfd.global/knowledge-hub/example-tnfd-reporting/) — 416+ 家采纳者报告，支持按行业、国家、报告类型筛选，可直接下载 PDF。

您想深入了解哪个维度？
```

**场景 4：获取报告 PDF**
```
用户：我想看隆基的 TNFD 报告 PDF。

Skill: 好的，这是隆基 TNFD 报告的获取方式：

1. **TNFD 官方报告库**：https://tnfd.global/knowledge-hub/example-tnfd-reporting/
   - 搜索 "LONGi" 或 "隆基"
   - 可直接下载 PDF

2. **隆基官网**：https://www.longi.com/cn/news/tnfd-report/
   - 中文版本地下载

需要我帮您打开链接吗？
```

---

## 用户引导流程

```
┌─────────────────────────────────────────────────────┐
│          TNFD Skill 用户引导流程                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Step 1 → TNFD 是什么？（1 分钟了解）                 │
│     ↓ 阅读：references/tnfd-leap-complete-guide.md  │
│                                                     │
│  Step 2 → 谁需要披露？（判断你是否需要）             │
│     ↓ 阅读：references/tnfd-leap-complete-guide.md  │
│                                                     │
│  Step 3 → LEAP 四阶段详解（如何做）                  │
│     ↓ 阅读：references/tnfd-leap-complete-guide.md  │
│                                                     │
│  Step 4 → 数据源清单（去哪找数据）                   │
│     ↓ 阅读：references/data-sources-registration-guide.md │
│                                                     │
│  Step 5 → 注册指南（如何获取数据）                   │
│     ↓ 阅读：references/data-sources-registration-guide.md │
│                                                     │
│  Step 6 → 行业指南（你的行业特殊要求）               │
│     ↓ 阅读：references/industry-guidance.md         │
│                                                     │
│  Step 7 → 披露模板（报告怎么写）                     │
│     ↓ 阅读：references/tnfd-leap-complete-guide.md  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 核心功能

### 1. 对标分析（Phase 0）⭐新增

**触发**：「TNFD 是什么」「我想做 TNFD 披露」「光伏行业 TNFD」

**输出**：
- 需求澄清（学习 vs 全流程）
- 行业标杆匹配（隆基/牧原等）
- 最佳实践提取
- 差距分析框架

**流程**：
```
Phase 0: Benchmark Analysis
├─ Step 1: 需求澄清（学习/培训/披露/对标）
├─ Step 2: 行业识别（匹配标杆企业）
├─ Step 3: 对标分析（最佳实践 + 差距）
└─ 输出：行业标杆清单 + 下一步建议
```

### 2. TNFD 框架问答

**触发**：「TNFD 是什么」「LEAP 怎么做」

**输出**：
- LEAP 四阶段详解
- 14 项披露建议解读
- 与 TCFD 对比

### 2. LEAP 四阶段引导

| 阶段 | Prompt | 输出物 |
|------|--------|--------|
| **Locate** | `prompts/01-locate.md` | 资产坐标清单 + 空间风险初步评估 |
| **Evaluate** | `prompts/02-evaluate.md` | 行业依赖矩阵 + 影响驱动因素清单 |
| **Assess** | `prompts/03-assess.md` | 风险登记册 + 机遇清单 + 财务影响量化 |
| **Prepare** | `prompts/04-prepare.md` | TNFD 报告草稿 + 响应策略 + 目标设定 |
| **Assurance** | `prompts/05-assurance.md` | 红旗清单 + 模拟审计意见 + 改进路线图 |

### 4. 数据源推荐

**触发**：「数据从哪来」「ENCORE 怎么下载」

**输出**：
- ENCORE、WDPA、IPE 等数据源清单
- 注册和下载步骤
- 数据质量检查清单

### 5. 行业特定指导

**触发**：「金融行业 TNFD」「农业怎么做」

**输出**：
- 行业指南下载链接
- 行业特定指标
- 行业案例参考（隆基/牧原）

### 5. 行业特定指导

**触发**：「金融行业 TNFD」「农业怎么做」

**输出**：
- 行业指南下载链接
- 行业特定指标
- 行业案例参考（隆基/牧原）

### 6. 报告生成辅助

**触发**：「帮我写 TNFD 报告」「披露模板」

**输出**：
- 14 项披露建议覆盖检查
- 报告结构模板
- 审计视角红旗清单

### 7. 四大方法论对标

**触发**：「四大怎么做」「安永 CCaSS」

**输出**：
- 四大方法论对照表
- 安永 CCaSS 流程
- CASS-ESG 6.0 整合

### 8. 审计检查

**触发**：「披露完整吗」「审计会查什么」

**输出**：
- 14 项覆盖检查
- 数据质量验证
- 模拟审计意见（无保留/保留/无法表示）

---

## 文档结构

```
skill/
├── SKILL.md                          # 主技能文件（触发词 + 核心协议）
└── references/
    ├── tnfd-leap-complete-guide.md   # LEAP 框架完整指南（Step 1-3-7）
    ├── data-sources-registration-guide.md  # 数据源注册指南（Step 4-5）
    ├── industry-guidance.md          # 行业指南汇总（Step 6）
    ├── big4-methodologies.md         # 四大方法论对照
    └── china-esg-standards.md        # 中国 ESG 标准体系
```

---

## 核心参考文档速查

| 文档 | 用途 | 阅读时间 |
|------|------|---------|
| `tnfd-leap-complete-guide.md` | TNFD 入门 + LEAP 详解 | 15 分钟 |
| `data-sources-registration-guide.md` | 数据下载操作手册 | 10 分钟 |
| `industry-guidance.md` | 行业特定指南 | 5-10 分钟 |
| `big4-methodologies.md` | 四大方法论对照 | 5 分钟 |
| `china-esg-standards.md` | 中国标准体系 | 5 分钟 |

---

## 典型使用场景

### 场景 1：首次接触 TNFD

```
用户：我是 ESG 专员，老板让我做 TNFD 披露，从哪开始？

Skill: 建议按 LEAP 四阶段进行：

1. Locate（1-2 周）：收集资产坐标，识别生态敏感区
2. Evaluate（1-2 周）：用 ENCORE 查询行业依赖/影响
3. Assess（2-4 周）：量化财务风险
4. Prepare（2-4 周）：编写报告

你是哪个行业？我可以提供行业特定指南。
```

### 场景 2：数据获取困难

```
用户：WDPA 注册了但下载太慢，有替代数据源吗？

Skill: 替代方案：

1. 地理遥感生态网（http://www.gisrs.cn）- 中国保护区数据
2. 国家生态数据中心（http://nesdc.org.cn）- 中国生态数据
3. 联系 TNFD Skill 获取预下载的中国区域数据

需要我帮你整理中国保护区数据吗？
```

### 场景 3：行业特定问题

```
用户：我们是银行，TNFD 对金融行业有什么特殊要求？

Skill: 金融行业特殊要求：

1. 范围 3 排放（融资排放）需要披露
2. 贷款组合自然风险评估
3. 客户行业风险传导分析

TNFD 发布了金融行业附加指南，我发你下载链接。
```

### 场景 4：报告质量检查

```
用户：我们的 TNFD 报告写好了，能帮我看下完整吗？

Skill: 用 14 项披露建议检查清单逐项核对：

治理（2 项）：
□ 董事会监督自然风险
□ 管理层评估和管理风险

战略（2 项）：
□ 自然相关问题对业务的影响
□ 自然相关机遇的影响

...（共 14 项）

需要我提供完整检查清单吗？
```

---

## 与 TNFD 平台的关系

| 功能 | TNFD Skill | TNFD 平台（规划中） |
|------|-----------|------------------|
| 框架指导 | ✅ 完整 | ⚠️ 基础 |
| 数据下载 | ✅ 指南 + 链接 | ✅ 集成下载 |
| 空间分析 | ❌ 需外部工具 | ✅ 内置地图 |
| 报告生成 | ✅ 模板 + 检查 | ✅ 一键生成 |
| 审计视角 | ✅ 四大方法论 | ⚠️ 基础 |
| 价格 | 免费 | Freemium |

**建议**：
- 学习 TNFD → 用 Skill
- 获取数据 → 用 Skill 指南
- 生成报告 → Skill 辅助 + 平台（如有）
- 正式鉴证 → 四大事务所

---

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| 0.1.0 | 2026-04-18 | 初始版本：核心框架 + 四大方法论 + 中国标准 |
| 0.2.0 | 计划中 | Prompt 模板 + 数据文件集成 |

---

## 反馈与支持

**问题反馈**：
- GitHub Issues（如开源）
- 邮件联系

**贡献指南**：
- 欢迎提交行业案例
- 欢迎补充数据源
- 欢迎改进 Prompt 模板

---

## 免责声明

本 Skill 基于 TNFD v1.0 官方框架和四大公开方法论提供指导，**不构成正式审计或鉴证意见**。正式披露建议：
1. 完成完整的 LEAP 评估
2. 进行第三方验证
3. 咨询专业审计机构

---

## 许可证

MIT License

---

## GitHub 部署

### 上传到 GitHub

```bash
cd ~/Desktop/TNFD/skill

# 1. 初始化 Git
git init

# 2. 创建 .gitignore（排除大型原始数据）
cat > .gitignore << EOF
# 大型原始数据
data/encore_raw/*.csv
data/encore_processed/*.json

# Python 缓存
__pycache__/
*.pyc

# 本地配置
.env
EOF

# 3. 添加文件
git add -A
git commit -m "Initial commit: TNFD Disclosure Skill"

# 4. 创建 GitHub 仓库并推送
# (在 GitHub 上创建仓库后)
git remote add origin https://github.com/YOUR_USERNAME/tnfd-disclosure-skill.git
git push -u origin main
```

### 用户安装

```bash
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/tnfd-disclosure-skill.git
cd tnfd-disclosure-skill

# 初始化数据
python3 scripts/process_encore_data.py

# 符号链接到 Hermes
ln -s $(pwd) ~/.Hermes/skills/tnfd-disclosure
```

---

## 参考文档

- [TNFD 官方](https://tnfd.global)
- [ENCORE 数据库](https://encorenature.org)
- [CASS-ESG 6.0](http://www.cass-ess.org.cn)
- [安永 CCaSS](https://www.ey.com/zh_cn/services/climate-change-sustainability-services)
