#!/usr/bin/env python3
"""
ENCORE 数据处理脚本
将原始 CSV 转换为 Skill 可用的 JSON 格式
"""

import csv
import json
from pathlib import Path

# 数据路径
ENCORE_RAW_DIR = Path(__file__).parent.parent / "data" / "encore_raw"
ENCORE_PROCESSED_DIR = Path(__file__).parent.parent / "data" / "encore_processed"

# 确保输出目录存在
ENCORE_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def read_csv(filename):
    """读取 CSV 文件"""
    filepath = ENCORE_RAW_DIR / filename
    if not filepath.exists():
        print(f"警告：文件不存在 {filepath}")
        return []
    
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        return list(reader)


def process_dependency_links():
    """处理依赖关系数据 (03. Dependency links.csv)"""
    print("处理依赖关系数据...")
    data = read_csv("03. Dependency links.csv")
    
    # 按行业分组
    by_industry = {}
    for row in data:
        isic_code = row.get('ISIC Unique code', 'Unknown')
        section = row.get('ISIC Section', 'Unknown')
        
        if section not in by_industry:
            by_industry[section] = []
        
        # 提取依赖项
        dependencies = []
        for key, value in row.items():
            if key not in ['ISIC Unique code', 'ISIC Section', 'ISIC Division', 
                          'ISIC Group', 'ISIC Class', 'ISIC level used for analysis', 'References']:
                if value and str(value).strip() and str(value).strip() != 'N/A':
                    dependencies.append({
                        'service': key,
                        'description': str(value)[:200],  # 截断描述
                        'level': 'high' if 'dependent' in str(value).lower() else 'medium'
                    })
        
        by_industry[section].append({
            'isic_code': isic_code,
            'division': row.get('ISIC Division', ''),
            'group': row.get('ISIC Group', ''),
            'class': row.get('ISIC Class', ''),
            'dependencies': dependencies[:10]  # 只保留前 10 个依赖
        })
    
    # 保存
    output_file = ENCORE_PROCESSED_DIR / "dependency_by_industry.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(by_industry, f, ensure_ascii=False, indent=2)
    
    print(f"  已保存 {len(by_industry)} 个行业分类到 {output_file}")
    return by_industry


def process_pressure_links():
    """处理影响关系数据 (05. Pressure links.csv)"""
    print("处理影响关系数据...")
    data = read_csv("05. Pressure links.csv")
    
    # 按行业分组
    by_industry = {}
    for row in data:
        isic_code = row.get('ISIC Unique code', 'Unknown')
        section = row.get('ISIC Section', 'Unknown')
        
        if section not in by_industry:
            by_industry[section] = []
        
        # 提取影响项
        pressures = []
        for key, value in row.items():
            if key not in ['ISIC Unique code', 'ISIC Section', 'ISIC Division', 
                          'ISIC Group', 'ISIC Class', 'ISIC level used for analysis', 'References']:
                if value and str(value).strip() and str(value).strip() != 'N/A':
                    pressures.append({
                        'pressure': key,
                        'description': str(value)[:200],
                        'level': 'high' if 'significant' in str(value).lower() else 'medium'
                    })
        
        by_industry[section].append({
            'isic_code': isic_code,
            'division': row.get('ISIC Division', ''),
            'pressures': pressures[:10]  # 只保留前 10 个影响
        })
    
    # 保存
    output_file = ENCORE_PROCESSED_DIR / "pressure_by_industry.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(by_industry, f, ensure_ascii=False, indent=2)
    
    print(f"  已保存 {len(by_industry)} 个行业分类到 {output_file}")
    return by_industry


def process_ecosystem_services():
    """处理生态系统服务定义 (02. Ecosystem services definitions.csv)"""
    print("处理生态系统服务定义...")
    data = read_csv("02. Ecosystem services definitions.csv")
    
    services = []
    for row in data:
        services.append({
            'name': row.get('Ecosystem service', ''),
            'category': row.get('Category', ''),
            'definition': row.get('Definition', '')[:300]
        })
    
    # 保存
    output_file = ENCORE_PROCESSED_DIR / "ecosystem_services.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(services, f, ensure_ascii=False, indent=2)
    
    print(f"  已保存 {len(services)} 个生态系统服务到 {output_file}")
    return services


def create_industry_summary():
    """创建行业摘要（用于 Skill 快速查询）"""
    print("创建行业摘要...")
    
    dependency_data = process_dependency_links()
    pressure_data = process_pressure_links()
    
    summary = {}
    for section in dependency_data.keys():
        summary[section] = {
            'company_count': len(dependency_data[section]),
            'sample_companies': [c['isic_code'] for c in dependency_data[section][:5]],
            'top_dependencies': [],
            'top_pressures': []
        }
        
        # 统计最常见的依赖
        dep_count = {}
        for company in dependency_data[section]:
            for dep in company.get('dependencies', []):
                dep_name = dep.get('service', 'Unknown')
                dep_count[dep_name] = dep_count.get(dep_name, 0) + 1
        
        summary[section]['top_dependencies'] = sorted(
            dep_count.items(), key=lambda x: x[1], reverse=True
        )[:10]
    
    # 保存
    output_file = ENCORE_PROCESSED_DIR / "industry_summary.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"  已保存行业摘要到 {output_file}")
    return summary


def main():
    """主函数"""
    print("=" * 60)
    print("ENCORE 数据处理脚本")
    print("=" * 60)
    
    # 检查原始数据
    if not ENCORE_RAW_DIR.exists():
        print(f"错误：原始数据目录不存在 {ENCORE_RAW_DIR}")
        print("请先将 ENCORE CSV 文件复制到该目录")
        return
    
    # 处理数据
    process_ecosystem_services()
    create_industry_summary()
    
    print("=" * 60)
    print("处理完成！")
    print(f"输出目录：{ENCORE_PROCESSED_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
