# TNFD 数据源注册与下载完整指南

> 实测时间：2026 年 4 月 18 日  
> 用途：TNFD Skill 用户数据获取操作手册

---

## 数据源总览

| 数据源 | 用途 | 注册 | 下载大小 | 更新时间 | 难度 |
|--------|------|------|---------|---------|------|
| **ENCORE** | 行业依赖/影响矩阵 | ❌ 无需 | 2MB | 年度 | ⭐ |
| **WDPA** | 全球保护区边界 | ✅ 免费 | 600MB | 月度 | ⭐⭐ |
| **WRI Aqueduct** | 水风险数据 | ✅ 免费 | 50-200MB | 年度 | ⭐⭐ |
| **IPE 蔚蓝地图** | 中国污染数据 | ❌ 无需 | - | 实时 | ⭐ |
| **国家生态数据中心** | 中国生态数据 | ⚠️ 部分需申请 | 不定 | 不定期 | ⭐⭐⭐ |
| **地理遥感生态网** | 中国土地利用 | ✅ 联系获取 | 不定 | 不定期 | ⭐⭐⭐ |

---

## 1. ENCORE 数据库（最常用）

**用途**：查询各行业的生态系统依赖和影响矩阵  
**难度**：⭐（最简单）  
**时间**：5 分钟

### 下载步骤

**步骤 1**：打开官网
```
https://encorenature.org/en/data-and-methodology/methodology
```

**步骤 2**：找到下载区域
- 滚动到页面中部
- 找到「Download the updated ENCORE knowledge base」标题

**步骤 3**：点击下载
- 点击「DOWNLOAD」按钮（蓝色）
- 自动开始下载 `ENCORE_DataFiles_Oct-2025.zip`

**步骤 4**：解压文件
```bash
# Mac/Linux
unzip ENCORE_DataFiles_Oct-2025.zip

# Windows
右键 → 解压到当前文件夹
```

**步骤 5**：查看文件结构
```
Updated ENCORE knowledge base September 2025/
├── ENCORE files/
│   ├── 01. Overview - IMPORTANT (READ ME).xlsx
│   ├── 02. Ecosystem services definitions.csv
│   ├── 03. Dependency links.csv          ← 核心：依赖矩阵
│   ├── 04. Pressure definitions.csv
│   ├── 05. Pressure links.csv            ← 核心：影响矩阵
│   ├── 06. Dependency mat ratings.csv
│   ├── 07. Pressure mat ratings.csv
│   └── ...
└── Crosswalk tables/
```

### 核心文件说明

| 文件 | 内容 | 用途 |
|------|------|------|
| `03. Dependency links.csv` | 行业 × 生态系统服务依赖关系 | Evaluate 阶段核心数据 |
| `05. Pressure links.csv` | 行业 × 影响驱动因素关系 | Evaluate 阶段核心数据 |
| `06. Dependency mat ratings.csv` | 依赖重要性评级 | 重要性排序 |
| `07. Pressure mat ratings.csv` | 影响重要性评级 | 重要性排序 |
| `02. Ecosystem services definitions.csv` | 25 种生态系统服务定义 | 术语参考 |

### 如何使用（Excel 示例）

1. 打开 `03. Dependency links.csv`
2. 查找你的行业 ISIC 代码（A 列）
3. 横向查看各生态系统服务的依赖描述
4. 标记「high」「medium」「low」依赖等级

### 常见问题

**Q: 找不到我的行业代码怎么办？**
A: ENCORE 使用 ISIC 行业分类，可对照：
- ISIC A = 农业
- ISIC B = 采矿
- ISIC C = 制造
- ISIC D = 电力供应
- ISIC F = 建筑
- ISIC K = 金融

**Q: 文件太大打不开怎么办？**
A: 用 Excel 打开时选择「仅加载前 1000 行」，或用 Google Sheets

---

## 2. WDPA Protected Planet（保护区数据）

**用途**：获取全球自然保护区边界矢量数据  
**难度**：⭐⭐  
**时间**：10 分钟

### 注册步骤

**步骤 1**：打开官网
```
https://www.protectedplanet.net
```

**步骤 2**：点击登录
- 点击右上角「Sign In」

**步骤 3**：创建账户
- 点击「Create an account」
- 填写：
  - Email（建议用工作邮箱）
  - Password（8 位以上）
  - First Name
  - Last Name
  - Country
  - Organization（公司/机构名称）
  - User type（选「Private sector」或「Academic」）

**步骤 4**：验证邮箱
- 查收验证邮件
- 点击验证链接

**步骤 5**：登录账户
- 返回官网登录

### 下载步骤

**步骤 1**：进入下载页面
```
https://www.protectedplanet.net/en/theprotectedplanet-database
```

**步骤 2**：选择数据类型
- WDPA Shapefile（推荐，GIS 软件用）
- WDPA GeoJSON（Web 开发用）
- WDPA Points Only（仅点位，小文件）

**步骤 3**：同意使用条款
- 阅读 Terms of Use
- 勾选「I agree to the terms」

**步骤 4**：开始下载
- 点击「Download」
- 文件大小约 600MB
- 下载时间取决于网速（约 5-20 分钟）

**步骤 5**：解压文件
```bash
# 解压后包含：
WDPA_WDOECM_Dec2024_Public_shp/
├── WDPA_WDOECM_Dec2024_Public_shp-polygons.shp
├── WDPA_WDOECM_Dec2024_Public_shp-polygons.dbf
├── WDPA_WDOECM_Dec2024_Public_shp-polygons.shx
└── WDPA_WDOECM_Dec2024_Public_README.pdf
```

### 数据说明

| 字段 | 含义 |
|------|------|
| NAME | 保护区名称 |
| ISO3 | 国家代码（CHN=中国） |
| IUCN_CAT | 保护区类别（I-VI） |
| REP_AREA | 保护区面积（km²） |
| STATUS | 状态（Designated=官方指定） |

### 中国数据提取（QGIS 示例）

1. 打开 QGIS
2. 加载 `WDPA_WDOECM_Dec2024_Public_shp-polygons.shp`
3. 右键图层 → 筛选
4. 输入：`"ISO3" = 'CHN'`
5. 导出筛选后的图层为中国保护区数据

### 常见问题

**Q: 下载速度太慢怎么办？**
A: 
- 使用下载工具（如 IDM、迅雷）
- 或联系 TNFD Skill 获取预下载的中国区域数据

**Q: Shapefile 打不开怎么办？**
A: 
- 安装 QGIS（免费）：https://qgis.org
- 或用 ArcGIS、Global Mapper 等专业软件

---

## 3. WRI Aqueduct（水风险数据）

**用途**：获取全球水风险评级数据  
**难度**：⭐⭐  
**时间**：8 分钟

### 注册步骤

**步骤 1**：打开官网
```
https://www.wri.org/aqueduct
```

**步骤 2**：点击获取数据
- 点击「Get the Data」或「Download」

**步骤 3**：填写表单
- First Name
- Last Name
- Email
- Organization
- Country
- Intended use（选择用途：Academic/Commercial/Government）

**步骤 4**：提交
- 点击「Submit」
- 自动获得下载链接

### 下载步骤

**步骤 1**：选择数据
- Aqueduct Water Risk Atlas
- Aqueduct Floods
- Aqueduct Food（农业用水）

**步骤 2**：选择格式
- CSV（表格数据）
- GeoTIFF（栅格地图）
- Shapefile（矢量数据）

**步骤 3**：下载
- 点击对应格式链接
- 文件大小约 50-200MB

### 核心指标说明

| 指标 | 含义 | 风险等级 |
|------|------|---------|
| Baseline Water Stress | 基线水压力 | 0-5（5 最高风险） |
| Interannual Variability | 年际变异 | 水供应稳定性 |
| Seasonal Variability | 季节变异 | 旱季/雨季差异 |
| Groundwater Table | 地下水位 | 下降=高风险 |

### 如何使用（Excel 示例）

1. 打开下载的 CSV 文件
2. 查找你的资产所在国家/地区
3. 查看 `Baseline Water Stress` 列
4. 评分 ≥4 = 高水风险区域

### 常见问题

**Q: 数据是栅格格式，怎么用？**
A: 
- 用 QGIS 打开 GeoTIFF
- 或用 ArcGIS 提取特定位置的值
- 或联系 TNFD Skill 获取点位查询服务

---

## 4. IPE 蔚蓝地图（中国污染数据）

**用途**：查询中国企业环境违规记录  
**难度**：⭐（最简单）  
**时间**：3 分钟

### 无需注册，直接查询

**步骤 1**：打开官网
```
https://www.ipe.org.cn
```

**步骤 2**：搜索企业
- 在搜索框输入企业名称
- 或输入统一社会信用代码

**步骤 3**：查看结果
- 环境行政处罚
- 排污许可信息
- 企业环境信用评价

### API 使用（开发者）

**API 文档**：
```
https://www.ipe.org.cn/api
```

**示例请求**：
```bash
# 搜索企业
curl "https://api.ipe.org.cn/v1/companies?keyword=企业名称"

# 获取企业违规记录
curl "https://api.ipe.org.cn/v1/companies/{id}/violations"
```

**注意**：API 需要申请 Key，联系 IPE 获取

### 常见问题

**Q: 找不到我的企业怎么办？**
A: 
- 尝试简称或曾用名
- 检查统一社会信用代码
- 可能企业暂无公开环境记录

---

## 5. 国家生态数据中心（中国生态数据）

**用途**：获取中国区域生态系统观测数据  
**难度**：⭐⭐⭐  
**时间**：15-30 分钟

### 浏览数据

**步骤 1**：打开官网
```
http://nesdc.org.cn
```

**步骤 2**：浏览数据目录
- 首页 → 数据资源
- 按台站/专项网/项目分类

**步骤 3**：查看数据详情
- 点击数据集名称
- 查看数据描述、时间范围、格式

### 下载数据

**直接下载**：
- 部分数据可直接下载（点击「下载」按钮）

**申请下载**：
1. 点击「申请数据」
2. 填写：
   - 姓名
   - 单位
   - 邮箱
   - 数据用途说明（研究/商业）
3. 等待审核（1-5 个工作日）
4. 审核通过后邮件发送下载链接

### 核心数据集推荐

| 数据集 | 用途 | 格式 |
|--------|------|------|
| 中国植被数据产品集（CVP） | 植被覆盖分析 | GeoTIFF |
| 中国陆地生态系统干扰数据集 | 人类活动影响 | GeoTIFF |
| ChinaFLUX 通量数据 | 碳通量观测 | CSV |
| 中国土壤有机碳密度数据集 | 土壤碳储量 | GeoTIFF |

### 常见问题

**Q: 申请一直不通过怎么办？**
A: 
- 检查邮箱是否填写正确
- 重新提交申请
- 联系数据中心：nesdc@igsnrr.ac.cn

---

## 6. 地理遥感生态网（中国土地利用）

**用途**：获取中国土地利用、植被指数等数据  
**难度**：⭐⭐⭐  
**时间**：需联系获取

### 联系方式

**官网**：
```
http://www.gisrs.cn
```

**联系方式**：
- QQ：416498894
- 邮箱：gisrscn@126.com
- 地址：北京市西城区宣武门外大街 88 号

### 获取流程

1. 添加 QQ 或发送邮件
2. 说明数据需求（区域、类型、用途）
3. 获取报价（部分数据收费）
4. 付款后获取数据

### 核心数据推荐

| 数据 | 分辨率 | 价格参考 |
|------|--------|---------|
| 土地利用遥感监测 | 30m | 免费/低价 |
| NDVI 植被指数 | 1km | 免费 |
| 自然保护区分布 | 矢量 | 免费 |
| 高分辨率影像 | 2-10m | 收费 |

---

## 数据质量检查清单

下载数据后，用以下清单检查：

```
□ 数据完整性：是否覆盖所有需要的区域？
□ 数据时效性：是否是最近 12 个月的数据？
□ 数据格式：是否能被我的工具打开？
□ 坐标系统：是否与我的其他数据对齐？
□ 许可协议：是否可以用于我的用途（商业/研究）？
□ 数据来源：是否可以在报告中引用？
```

---

## 数据管理建议

### 文件命名规范

```
建议格式：数据源_数据类型_日期_区域.格式

示例：
- ENCORE_DependencyLinks_202510_Global.csv
- WDPA_ProtectedAreas_202412_China.geojson
- Aqueduct_WaterRisk_2024_Global.tif
```

### 文件夹结构

```
TNFD_Data/
├── 01_Raw/              # 原始下载数据
│   ├── ENCORE/
│   ├── WDPA/
│   ├── Aqueduct/
│   └── IPE/
├── 02_Processed/        # 处理后数据
│   ├── China_Protected_Areas.geojson
│   └── Asset_Risk_Scores.csv
└── 03_Output/           # 输出成果
    ├── Risk_Maps/
    └── Reports/
```

### 版本控制

- 每次更新数据时保留旧版本
- 在文件名中标注日期
- 维护数据更新日志

---

## 参考文档

- [ENCORE 方法论](https://encorenature.org/en/data-and-methodology/methodology)
- [WDPA 使用指南](https://www.protectedplanet.net/en/theprotectedplanet-database)
- [WRI Aqueduct 文档](https://www.wri.org/aqueduct)
- [IPE API 文档](https://www.ipe.org.cn/api)
- [国家生态数据中心](http://nesdc.org.cn)
