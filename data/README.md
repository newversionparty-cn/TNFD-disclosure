# TNFD Skill 数据目录

> 用途：存放 Skill 运行所需的本地数据文件  
> 最后更新：2026 年 4 月 19 日

---

## 目录结构

```
data/
├── encore_raw/                    # ENCORE 原始 CSV 数据
│   ├── 02. Ecosystem services definitions.csv
│   ├── 03. Dependency links.csv
│   ├── 04. Pressure definitions.csv
│   ├── 05. Pressure links.csv
│   └── ...
│
├── encore_processed/              # ENCORE 处理后 JSON 数据
│   ├── ecosystem_services.json    # 48 个生态系统服务定义
│   ├── dependency_by_industry.json # 21 个行业依赖关系
│   ├── pressure_by_industry.json   # 21 个行业影响关系
│   └── industry_summary.json       # 行业摘要（快速查询）
│
├── tnfd_report_links.json         # TNFD 报告链接清单（JSON 格式）
│
├── nature_tools_leap_mapping.json # ENCORE / IBAT 在 LEAP 中的步骤映射
│
└── README.md                      # 本文件
```

---

## 数据来源

### ENCORE 数据

- **来源**：https://encorenature.org/en/data-and-methodology/methodology
- **版本**：September 2025
- **下载**：通过 ENCORE Methodology & Downloads 页面登录后下载 updated knowledge base
- **许可**：CC BY-SA 4.0

### TNFD 报告链接

- **来源**：https://tnfd.global/knowledge-hub/example-tnfd-reporting/
- **数量**：416+ 家采纳者
- **更新**：建议每季度同步一次

### ENCORE / IBAT 工具映射

- **来源**：
  - https://encorenature.org/en/data-and-methodology/methodology
  - https://www.ibat-alliance.org/data
- **文件**：`nature_tools_leap_mapping.json`
- **用途**：告诉 Agent 在 LEAP 哪一步使用 ENCORE 或 IBAT：
  - ENCORE：主要用于 Evaluate 的行业/活动依赖与压力筛查
  - IBAT：主要用于 Locate 的敏感地点和生物多样性筛查
- **边界**：IBAT 站点报告、GIS 下载、API、map tiles 和派生数据可能需要许可；不得把公开介绍页当作站点级证据。

---

## 数据处理

### 运行处理脚本

```bash
cd ~/Desktop/TNFD/skill
python3 scripts/process_encore_data.py
```

### 输出说明

| 文件 | 内容 | 用途 |
|------|------|------|
| `ecosystem_services.json` | 48 个生态系统服务定义 | Evaluate 阶段查询 |
| `dependency_by_industry.json` | 21 个行业依赖关系 | Evaluate 阶段行业匹配 |
| `pressure_by_industry.json` | 21 个行业影响关系 | Evaluate 阶段行业匹配 |
| `industry_summary.json` | 行业摘要统计 | 快速查询/对标分析 |
| `tnfd_report_links.json` | 报告链接清单 | 对标分析阶段发送 PDF |
| `nature_tools_leap_mapping.json` | ENCORE / IBAT LEAP 映射 | 数据源选择和阶段路由 |

---

## 使用示例

### Skill 内部调用

```python
# 读取 ENCORE 处理后的数据
import json
with open('data/encore_processed/dependency_by_industry.json') as f:
    dependency_data = json.load(f)

# 查询某个行业的依赖关系
agriculture_deps = dependency_data.get('Agriculture, forestry and fishing', [])
```

### 发送报告链接

```python
# 读取报告链接清单
import json
with open('data/tnfd_report_links.json') as f:
    report_links = json.load(f)

# 获取光伏行业报告
solar_reports = report_links['industries']['solar_clean_energy']['companies']
```

---

## 数据更新

### ENCORE 数据更新

1. 访问 https://encorenature.org/en/data-and-methodology/methodology
2. 下载最新 ZIP 文件
3. 解压 CSV 到 `data/encore_raw/`
4. 运行 `python3 scripts/process_encore_data.py`

### TNFD 报告链接更新

1. 访问 https://tnfd.global/knowledge-hub/example-tnfd-reporting/
2. 筛选目标行业/国家
3. 更新 `data/tnfd_report_links.json`
4. 更新 `references/tnfd-report-links.md`

---

## 许可说明

- **ENCORE 数据**：CC BY-SA 4.0（需署名）
- **TNFD 报告链接**：公开信息，仅供学习参考
- **Skill 代码**：MIT License
