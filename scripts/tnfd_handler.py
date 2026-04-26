#!/usr/bin/env python3
"""
TNFD PUA Handler — 处理 /tnfd 指令并输出 Sprint Banner + KPI
"""

import json
import sys
from pathlib import Path
from datetime import datetime

TNFD_DIR = Path.home() / ".tnfd"
CONFIG_FILE = TNFD_DIR / "config.json"
STATE_FILE = TNFD_DIR / "project-state.json"
COMMANDS_FILE = TNFD_DIR / "commands.json"

# ─────────────────────────────────────────────────────────────
# 初始化目录和文件
# ─────────────────────────────────────────────────────────────

def init_tnfd():
    TNFD_DIR.mkdir(exist_ok=True)
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'w') as f:
            json.dump({
                "version": "1.0.0",
                "user_id": "default",
                "registered_at": datetime.now().isoformat(),
                "flavor": "alibaba",
                "current_project": None,
                "skill_config": {
                    "auto_trigger": True,
                    "pua_enabled": True,
                    "strict_mode": False
                }
            }, f, indent=2)
    if not STATE_FILE.exists():
        with open(STATE_FILE, 'w') as f:
            json.dump({"projects": {}, "last_updated": datetime.now().isoformat()}, f)
    if not COMMANDS_FILE.exists():
        print("⚠️ COMMANDS_FILE not found. Run this script from the skill directory.", file=sys.stderr)
        sys.exit(1)

# ─────────────────────────────────────────────────────────────
# 加载数据
# ─────────────────────────────────────────────────────────────

def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"projects": {}, "last_updated": datetime.now().isoformat()}

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {"flavor": "alibaba", "current_project": None}

def load_commands():
    with open(COMMANDS_FILE) as f:
        return json.load(f)

# ─────────────────────────────────────────────────────────────
# Banner 输出
# ─────────────────────────────────────────────────────────────

def sprint_banner(command, phase_info=None):
    """输出 Sprint Banner"""
    flavor_map = {
        "alibaba": "🟠 阿里味",
        "bytedance": "🟡 字节味",
        "huawei": "🔴 华为味",
    }
    flavor = load_config().get("flavor", "alibaba")
    flavor_str = flavor_map.get(flavor, "🟠 阿里味")
    
    state = load_state()
    current_project = load_config().get("current_project")
    
    project_info = "无活跃项目"
    leap_status = "—"
    
    if current_project and current_project in state.get("projects", {}):
        proj = state["projects"][current_project]
        project_info = proj.get("name", current_project)
        leap = proj.get("leap_complete", [])
        leap_status = " → ".join(leap) if leap else "未开始"
    
    banner = f"""
┌─────────┬────────────────────────────────────────────────────────┐
│ 📋 任务 │ {command[:50]:<50} │
├─────────┼────────────────────────────────────────────────────────┤
│ 🔥 味道 │ {flavor_str:<50} │
├─────────┼────────────────────────────────────────────────────────┤
│ ⚡ 压力 │ L0 · 信任期                                        │
├─────────┼────────────────────────────────────────────────────────┤
│ 📦 项目 │ {project_info:<50} │
├─────────┼────────────────────────────────────────────────────────┤
│ 📊 LEAP │ {leap_status:<50} │
└─────────┴────────────────────────────────────────────────────────┘
"""
    print(banner)

def status_banner():
    """输出项目状态 Banner"""
    state = load_state()
    config = load_config()
    current_project = config.get("current_project")
    
    if not current_project or current_project not in state.get("projects", {}):
        print("""
┌─────────────────────────────────────────────────────────────┐
│  📦 TNFD 项目状态                                           │
│                                                              │
│  当前无活跃项目                                              │
│                                                              │
│  使用 /tnfd new 创建新项目                                    │
│  使用 /tnfd benchmark 开始对标分析                            │
└─────────────────────────────────────────────────────────────┘
""")
        return
    
    proj = state["projects"][current_project]
    
    leap = proj.get("leap_complete", [])
    phase_order = ["locate", "evaluate", "assess", "prepare", "assurance"]
    leap_icons = []
    for p in phase_order:
        if p in leap:
            leap_icons.append(f"✅ {p.capitalize()}")
        else:
            leap_icons.append(f"⬜ {p.capitalize()}")
    
    risks = proj.get("risks_found", [])
    data_quality = proj.get("data_quality", "B")
    
    banner = f"""
┌─────────────────────────────────────────────────────────────┐
│  📦 TNFD 项目状态                                           │
│                                                              │
│  项目：{proj.get('name', current_project):<45} │
│  行业：{proj.get('industry', '未设置'):<46} │
│  阶段：{proj.get('current_phase', 'phase0'):<45} │
│                                                              │
│  LEAP 进度：                                                │
│  {' │ '.join(leap_icons[:3])}                                 │
│  {' │ '.join(leap_icons[3:])}                                 │
│                                                              │
│  发现风险：{len(risks):<3} 个                                       │
│  数据质量：{data_quality:<3} 级                                       │
└─────────────────────────────────────────────────────────────┘
"""
    print(banner)

def kpi_card(tnfd_count=0, risks_found=0, data_quality="B", leap_complete=None):
    """输出 KPI 卡"""
    if leap_complete is None:
        leap_complete = []
    
    leap_progress = len(leap_complete) / 5
    
    quality_map = {"A": "⭐⭐⭐⭐⭐", "B": "⭐⭐⭐⭐", "C": "⭐⭐⭐", "D": "⭐⭐", "F": "⭐"}
    quality_stars = quality_map.get(data_quality, "⭐⭐⭐")
    
    # 计算综合评分
    base_score = min(10, tnfd_count * 2 + len(leap_complete) * 1.5 + risks_found * 0.5)
    score = min(5.0, base_score)
    
    score_emoji = "🥇" if score >= 4.5 else "🥈" if score >= 3.5 else "🥉" if score >= 2.5 else "📉"
    
    kpi = f"""
┌─────────────────────────────────────────────────────────────┐
│  📊 TNFD KPI 报告卡                                         │
│                                                              │
│  本次会话绩效：                                              │
│  · 完成任务数：{tnfd_count:<3}                                        │
│  · LEAP 进度：{'█' * int(leap_progress * 10)}{'░' * (10 - int(leap_progress * 10))} {len(leap_complete)}/5       │
│  · 发现风险数：{risks_found:<3}                                        │
│  · 数据质量：{quality_stars}                                │
│                                                              │
│  综合评级：{score_emoji} {score:.1f}                                               │
│  「这才像个 P8 的样子。」                                      │
└─────────────────────────────────────────────────────────────┘
"""
    print(kpi)

def help_card():
    """输出帮助卡片"""
    print("""
┌─────────────────────────────────────────────────────────────┐
│  🌶️ TNFD 指令系统                                           │
│                                                              │
│  核心指令：                                                  │
│  /tnfd          启动 TNFD 助手                              │
│  /tnfd new      新建 TNFD 项目                              │
│  /tnfd status   查看项目状态                                │
│  /tnfd kpi      查看 KPI 报告                               │
│                                                              │
│  LEAP 流程：                                                  │
│  /tnfd benchmark  Phase 0：对标分析                          │
│  /tnfd locate     Phase 1：定位                             │
│  /tnfd evaluate   Phase 2：评价                             │
│  /tnfd assess     Phase 3：评估                             │
│  /tnfd prepare    Phase 4：准备                             │
│  /tnfd audit      Phase 5：审计检查                         │
│                                                              │
│  报告生成：                                                  │
│  /tnfd report    生成 TNFD 报告                             │
│                                                              │
│  项目管理：                                                  │
│  /tnfd save      保存项目状态                               │
│  /tnfd reset     重置项目                                   │
└─────────────────────────────────────────────────────────────┘
""")

# ─────────────────────────────────────────────────────────────
# 状态更新
# ─────────────────────────────────────────────────────────────

def update_phase(phase, data=None):
    """更新项目阶段"""
    state = load_state()
    config = load_config()
    current_project = config.get("current_project")
    
    if not current_project:
        print("⚠️ 没有活跃项目。请先使用 /tnfd new 创建项目。")
        return False
    
    if current_project not in state["projects"]:
        state["projects"][current_project] = {
            "name": current_project,
            "industry": "未设置",
            "current_phase": phase,
            "leap_complete": [],
            "risks_found": [],
            "data_quality": "B",
            "created_at": datetime.now().isoformat()
        }
    
    proj = state["projects"][current_project]
    proj["current_phase"] = phase
    proj["last_updated"] = datetime.now().isoformat()
    
    if data:
        for key, value in data.items():
            proj[key] = value
    
    # 标记 LEAP 完成
    if phase not in proj["leap_complete"] and phase in ["locate", "evaluate", "assess", "prepare", "assurance"]:
        proj["leap_complete"].append(phase)
    
    state["projects"][current_project] = proj
    state["last_updated"] = datetime.now().isoformat()
    
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    
    return True

def create_project(name, industry):
    """创建新项目"""
    state = load_state()
    config = load_config()
    
    project_id = f"project_{len(state['projects']) + 1}"
    
    state["projects"][project_id] = {
        "id": project_id,
        "name": name,
        "industry": industry,
        "current_phase": "phase0",
        "leap_complete": [],
        "risks_found": [],
        "data_quality": "B",
        "created_at": datetime.now().isoformat(),
        "last_updated": datetime.now().isoformat()
    }
    state["last_updated"] = datetime.now().isoformat()
    
    config["current_project"] = project_id
    
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)
    
    return project_id

# ─────────────────────────────────────────────────────────────
# 主入口
# ─────────────────────────────────────────────────────────────

def main():
    init_tnfd()
    
    if len(sys.argv) < 2:
        help_card()
        return
    
    command = sys.argv[1].lower()
    
    if command == "/tnfd" or command == "start":
        sprint_banner("启动 TNFD 助手")
        print("> 收到需求，对齐目标，进入 sprint。因为信任所以简单——别让信任你的人失望。")
        print("> 请告诉我你想做什么：")
        print("   /tnfd new — 新建项目")
        print("   /tnfd status — 查看状态")
        print("   /tnfd benchmark — 开始对标分析")
    
    elif command == "status":
        status_banner()
    
    elif command == "kpi":
        state = load_state()
        config = load_config()
        current_project = config.get("current_project")
        tnfd_count = len(state.get("projects", {}))
        risks_found = 0
        data_quality = "B"
        leap_complete = []
        if current_project and current_project in state.get("projects", {}):
            proj = state["projects"][current_project]
            risks_found = len(proj.get("risks_found", []))
            data_quality = proj.get("data_quality", "B")
            leap_complete = proj.get("leap_complete", [])
        kpi_card(tnfd_count, risks_found, data_quality, leap_complete)
    
    elif command in ["benchmark", "locate", "evaluate", "assess", "prepare", "assurance", "audit"]:
        phase_map = {
            "benchmark": "phase0",
            "locate": "locate",
            "evaluate": "evaluate",
            "assess": "assess",
            "prepare": "prepare",
            "assurance": "assurance",
            "audit": "assurance"
        }
        phase = phase_map.get(command, command)
        sprint_banner(f"/tnfd {command}", phase)
        update_phase(phase)
        print(f"> 进入 /tnfd {command}。请按照提示执行。")
    
    elif command == "help":
        help_card()
    
    else:
        print(f"⚠️ 未知指令：{command}")
        help_card()

if __name__ == "__main__":
    main()
