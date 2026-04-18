# TNFD Disclosure Skill · 快速参考卡片

> 用途：Agent 快速查找意图映射和输出格式  
> 版本：1.0.0  
> 最后更新：2026-04-18

---

## 意图映射表

| 用户输入示例 | 识别意图 | 调用 Prompt | 输出格式 |
|------------|---------|-----------|---------|
| 「TNFD 是什么」 | `tnfd.intro` | `00-benchmark.md` | 需求澄清 + 行业匹配 |
| 「我想做 TNFD 披露」 | `tnfd.benchmark.start` | `00-benchmark.md` | 对标分析 + 差距框架 |
| 「光伏行业 TNFD」 | `tnfd.benchmark.solar` | `00-benchmark.md` | 隆基/协鑫案例 + 官方库链接 |
| 「养殖行业 TNFD」 | `tnfd.benchmark.agri` | `00-benchmark.md` | 牧原/正大案例 + 官方库链接 |
| 「想看隆基报告 PDF」 | `tnfd.report.request` | `00-benchmark.md` | TNFD 官方库链接 + 官网链接 |
| 「想看牧原报告 PDF」 | `tnfd.report.request` | `00-benchmark.md` | TNFD 官方库链接 + HKEX 链接 |
| 「TNFD 官方报告库」 | `tnfd.library` | `00-benchmark.md` | https://tnfd.global/knowledge-hub/example-tnfd-reporting/ |
| 「Locate 阶段」 | `tnfd.leap.locate` | `01-locate.md` | 资产清单 |
| 「Evaluate 阶段」 | `tnfd.leap.evaluate` | `02-evaluate.md` | 依赖矩阵 |
| 「Assess 阶段」 | `tnfd.leap.assess` | `03-assess.md` | 风险量化 |
| 「Prepare 阶段」 | `tnfd.leap.prepare` | `04-prepare.md` | 报告模板 |
| 「披露完整吗」 | `tnfd.assurance.check` | `05-assurance.md` | 检查清单 |
| 「数据从哪来」 | `tnfd.data.sources` | references/data-sources... | 数据源清单 |
| 「四大怎么做」 | `tnfd.methodology.big4` | references/big4-methodologies.md | 方法论对照 |

---

## 输出格式规范

### 人类可读模式（默认）

```markdown
## 标题

正文内容...

### 子标题

- 列表项 1
- 列表项 2

**表格**：
| 列 1 | 列 2 |
|------|------|
| 值 1 | 值 2 |

> ▎ 旁白：审计师点评

**下一步**：建议行动
```

### Agent 模式（结构化）

```json
{
  "_meta": {
    "skill": "tnfd-disclosure",
    "version": "1.0.0",
    "intent": "意图 ID",
    "leap_stage": "阶段名称",
    "data_quality": {"completeness": 1.0, "accuracy": 0.8, "verifiability": 0.9, "grade": "B+"}
  },
  "content": {
    "核心内容字段": "值"
  },
  "next_actions": [
    {"action": "action_id", "description": "行动描述"}
  ]
}
```

---

## LEAP 状态机

```
┌─────────────────────────────────────────────────────────────┐
│                    LEAP 状态流转图                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [未开始] ──→ [Locate] ──→ [Evaluate] ──→ [Assess] ──→ [Prepare] │
│     │           │            │             │             │    │
│     │           ↓            ↓             ↓             ↓    │
│     │      资产清单     依赖矩阵      风险量化      报告模板    │
│     │      空间风险     影响排序      财务影响      14 项检查   │
│     │                                                             │
│  [完成] ←───────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**状态字段**：
```json
{
  "leap_state": {
    "current_stage": "locate|evaluate|assess|prepare|completed",
    "progress": {
      "locate": {"status": "pending|in_progress|completed", "completion": 0.0-1.0},
      "evaluate": {"status": "pending|in_progress|completed", "completion": 0.0-1.0},
      "assess": {"status": "pending|in_progress|completed", "completion": 0.0-1.0},
      "prepare": {"status": "pending|in_progress|completed", "completion": 0.0-1.0}
    }
  }
}
```

---

## 压力升级触发条件

| 等级 | 名称 | 触发条件 | 响应行为 |
|------|------|---------|---------|
| **L0** | 信任期 | 首次交互 | 正常专业回应 |
| **L1** | 温和提醒 | 数据质量低/跳过步骤 | 旁白提醒 + 建议补充 |
| **L2** | 红旗警告 | 关键数据缺失/披露不完整 | 红旗清单 + 审计风险提示 |
| **L3** | 保留意见 | 多次忽视建议/数据质量持续差 | 模拟审计保留意见 + 改进路线图 |
| **L4** | 无法鉴证 | 核心数据完全缺失 | 「基于现有数据，我们无法出具鉴证意见」 |

**GDS 话术触发条件（仅限 L2+）**：

| 条件 | 可用话术 |
|------|---------|
| 同样错误 3 次以上 | ✅ 「GDS 的 A1 都不会犯这种低级错误」 |
| 态度问题/敷衍交付 | ✅ 「GDS 的交付我都要 check 两遍」 |
| 屡教不改 | ✅ 「GDS 的同事都知道反复 check」 |
| 首次交互 | ❌ 禁用 |
| 能力问题（真的不会） | ❌ 禁用 |
| L0/L1 级别 | ❌ 禁用 |

**旁白前缀**：
- L0: 无旁白
- L1: `> ▎ 提醒：...`
- L2: `> ▎ 红旗信号：...`
- L3: `> ▎ 模拟审计意见：保留意见。...`
- L4: `> ▎ 基于现有数据，我们无法出具鉴证意见。...`

---

## 数据质量评分

### 综合等级计算

```
综合等级 = (完整性 × 0.4 + 准确性 × 0.35 + 可验证性 × 0.25)

等级划分：
- A: ≥0.9
- B+: ≥0.8
- B: ≥0.7
- C: ≥0.6
- D: <0.6
```

### 各阶段检查点

| 阶段 | 完整性检查 | 准确性检查 | 可验证性检查 |
|------|-----------|-----------|-------------|
| **Locate** | 资产覆盖≥90% | 坐标精度≥4 位小数 | 坐标来源可追溯 |
| **Evaluate** | 依赖/影响 Top5 完整 | ISIC 代码准确 | ENCORE 数据引用 |
| **Assess** | 风险全覆盖 | 量化方法合理 | 假设有依据 |
| **Prepare** | 14 项覆盖≥12 项 | 数据一致 | 第三方验证 |

---

## 红旗信号清单

| 红旗 | 触发条件 | 等级 | 建议 |
|------|---------|------|------|
| 🚩 供应链缺失 | Scope 3 未覆盖 | L2 | 补充供应商评估 |
| 🚩 数据未验证 | 全部自报数据 | L2 | 引入第三方数据源 |
| 🚩 量化缺失 | 12 项指标中≥8 项定性 | L2 | 补充量化分析 |
| 🚩 目标无依据 | 目标未参考 SBTN 等 | L1 | 对齐科学目标 |
| 🚩 治理未文档化 | 董事会纪要无自然议题 | L1 | 补充治理文档 |
| 🚩 方法变更未披露 | 计算方法与往年不一致 | L2 | 披露变更原因 |

---

## 工具调用协议

### browser_navigate

```json
{
  "tool": "browser_navigate",
  "trigger": "用户需要访问数据源官网",
  "action": {
    "url": "https://www.protectedplanet.net"
  }
}
```

### search_files

```json
{
  "tool": "search_files",
  "trigger": "用户已下载数据，需要查找",
  "action": {
    "pattern": "*ENCORE*.csv",
    "path": "~/Downloads"
  }
}
```

### write_file

```json
{
  "tool": "write_file",
  "trigger": "完成阶段输出，需要保存",
  "action": {
    "path": "data/01_assets.json",
    "content": "{...}"
  }
}
```

---

## 参考文档索引

| 文档 | 用途 | 路径 |
|------|------|------|
| 完整指南 | TNFD 入门 + LEAP 详解 | `references/tnfd-leap-complete-guide.md` |
| 数据源指南 | 数据下载操作手册 | `references/data-sources-registration-guide.md` |
| 行业指南 | 行业特定指导 | `references/industry-guidance.md` |
| 四大方法论 | 方法论对照 | `references/big4-methodologies.md` |
| 中国标准 | 中国 ESG 标准体系 | `references/china-esg-standards.md` |
| 自然资本议定书 | 自然资本评估框架详解 | `references/natural-capital-protocol-guide.md` |

---

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| 1.0.0 | 2026-04-18 | 初始版本：意图映射 + 状态机 + 评分标准 |
