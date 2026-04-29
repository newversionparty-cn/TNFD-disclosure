#!/usr/bin/env python3
"""
TNFD Engagement Handler — 处理 /tnfd 指令并输出 Sprint Banner + KPI
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

TNFD_DIR = Path(os.environ.get("TNFD_HOME", Path.cwd() / ".tnfd"))
CONFIG_FILE = TNFD_DIR / "config.json"
STATE_FILE = TNFD_DIR / "project-state.json"
COMMANDS_FILE = TNFD_DIR / "commands.json"
PHASE_ORDER = ["benchmark", "locate", "evaluate", "assess", "prepare", "assurance"]

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
                    "engagement_mode_enabled": True,
                    "strict_mode": False
                }
            }, f, indent=2, ensure_ascii=False)
    if not STATE_FILE.exists():
        with open(STATE_FILE, 'w') as f:
            json.dump({"projects": {}, "last_updated": datetime.now().isoformat()}, f, ensure_ascii=False)
    if not COMMANDS_FILE.exists():
        # Generate default commands.json — required for handler to function
        default_commands = {
            "version": "1.0.0",
            "generated_at": datetime.now().isoformat(),
            "commands": {
                "/tnfd": {"description": "启动 TNFD 助手", "phase": None},
                "/tnfd new": {"description": "新建 TNFD 项目", "phase": None},
                "/tnfd status": {"description": "查看项目状态", "phase": None},
                "/tnfd kpi": {"description": "生成 KPI 报告", "phase": None},
                "/tnfd benchmark": {"description": "Phase 0：对标分析", "phase": "phase0"},
                "/tnfd locate": {"description": "Phase 1：定位", "phase": "locate"},
                "/tnfd evaluate": {"description": "Phase 2：评价", "phase": "evaluate"},
                "/tnfd assess": {"description": "Phase 3：评估", "phase": "assess"},
                "/tnfd prepare": {"description": "Phase 4：准备披露", "phase": "prepare"},
                "/tnfd audit": {"description": "Phase 5：鉴证准备度检查", "phase": "assurance"},
                "/tnfd report": {"description": "生成报告包或缺口报告", "phase": None},
                "/tnfd save": {"description": "保存项目状态", "phase": None},
                "/tnfd reset": {"description": "重置项目", "phase": None}
            }
        }
        with open(COMMANDS_FILE, 'w') as f:
            json.dump(default_commands, f, indent=2, ensure_ascii=False)

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

def default_phase_status():
    return {phase: {"status": "not_started", "evidence_gate": "not_checked"} for phase in PHASE_ORDER}

# ─────────────────────────────────────────────────────────────
# Banner 输出
# ─────────────────────────────────────────────────────────────

def sprint_banner(command, phase_info=None):
    """输出 Sprint Banner"""
    state = load_state()
    config = load_config()
    current_project = config.get("current_project")
    
    project_info = "无活跃项目"
    leap_status = "—"
    
    if current_project and current_project in state.get("projects", {}):
        proj = state["projects"][current_project]
        project_info = proj.get("name", current_project)
        phase_status = proj.get("phase_status", default_phase_status())
        completed = [p for p in PHASE_ORDER if phase_status.get(p, {}).get("status") == "completed"]
        leap_status = " → ".join(completed) if completed else "未完成证据门禁"
    
    banner = f"""\
┌─────────┬────────────────────────────────────────────────────────┐
│ 📋 任务 │ {command[:50]:<50} │
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
    
    phase_status = proj.get("phase_status", default_phase_status())
    leap_icons = []
    for p in PHASE_ORDER:
        status = phase_status.get(p, {}).get("status", "not_started")
        if status == "completed":
            leap_icons.append(f"✅ {p}")
        elif status in ["in_progress", "evidence_pending"]:
            leap_icons.append(f"🟡 {p}")
        else:
            leap_icons.append(f"⬜ {p}")
    
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
    
    leap_progress = len(leap_complete) / len(PHASE_ORDER)
    
    quality_map = {"A": "⭐⭐⭐⭐⭐", "B": "⭐⭐⭐⭐", "C": "⭐⭐⭐", "D": "⭐⭐", "F": "⭐"}
    quality_stars = quality_map.get(data_quality, "⭐⭐⭐")
    
    # 计算综合评分
    base_score = min(10, tnfd_count * 2 + len(leap_complete) * 1.2 + risks_found * 0.5)
    score = min(5.0, base_score)
    
    score_emoji = "🥇" if score >= 4.5 else "🥈" if score >= 3.5 else "🥉" if score >= 2.5 else "📉"
    
    kpi = f"""\
┌─────────────────────────────────────────────────────────────┐
│  📊 TNFD KPI 报告卡                                         │
│                                                              │
│  本次会话绩效：                                              │
│  · 完成任务数：{tnfd_count:<3}                                        │
│  · 证据门禁进度：{'█' * int(leap_progress * 10)}{'░' * (10 - int(leap_progress * 10))} {len(leap_complete)}/{len(PHASE_ORDER)}  │
│  · 发现风险数：{risks_found:<3}                                        │
│  · 数据质量：{quality_stars}                                │
│                                                              │
│  内部进度评级：{score_emoji} {score:.1f}                                           │
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
│  /tnfd audit      Phase 5：鉴证准备度检查                   │
│                                                              │
│  报告生成：                                                  │
│  /tnfd report    生成报告包或缺口报告                       │
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
    """Mark a phase as in progress. Completion requires a separate evidence gate."""
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
            "phase_status": default_phase_status(),
            "risks_found": [],
            "data_quality": "B",
            "created_at": datetime.now().isoformat()
        }
    
    proj = state["projects"][current_project]
    proj["current_phase"] = phase
    proj["last_updated"] = datetime.now().isoformat()
    proj.setdefault("phase_status", default_phase_status())
    if phase in proj["phase_status"]:
        proj["phase_status"][phase] = {
            "status": "evidence_pending" if phase in ["prepare", "assurance"] else "in_progress",
            "evidence_gate": "not_checked",
            "updated_at": datetime.now().isoformat()
        }
    
    if data:
        for key, value in data.items():
            proj[key] = value
    
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
        "phase_status": default_phase_status(),
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

    raw = " ".join(sys.argv[1:]).strip().lower()
    # Handle "/tnfd" (bare) and "/tnfd status" (with subcommand)
    if raw.startswith("/tnfd"):
        parts = raw.split()
        if len(parts) == 1:
            command = "/tnfd"
        else:
            command = parts[1]  # e.g. "/tnfd status" -> "status"
    else:
        command = raw  # bare subcommand like "status"

    if command == "/tnfd" or command == "start" or command == "/tnfd":
        sprint_banner("启动 TNFD 助手")
        print("> 收到 TNFD 助手激活指令。请选择下一步操作：")
        print("> 请告诉我你想做什么：")
        print("   /tnfd new — 新建项目")
        print("   /tnfd status — 查看状态")
        print("   /tnfd benchmark — 开始对标分析")
        print(f"> 状态文件：{STATE_FILE}")
    
    elif command == "new":
        name = sys.argv[3] if len(sys.argv) > 3 else "未命名项目"
        industry = sys.argv[4] if len(sys.argv) > 4 else "未设置"
        project_id = create_project(name, industry)
        sprint_banner("新建 TNFD 项目")
        print(f"> 项目已创建：{project_id}。请补充公司名称、行业、披露范围和价值链边界。")
    
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
            phase_status = proj.get("phase_status", default_phase_status())
            leap_complete = [p for p in PHASE_ORDER if phase_status.get(p, {}).get("status") == "completed"]
        kpi_card(tnfd_count, risks_found, data_quality, leap_complete)
    
    elif command in ["benchmark", "locate", "evaluate", "assess", "prepare", "assurance", "audit"]:
        phase_map = {
            "benchmark": "benchmark",
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
        print(f"> 进入 /tnfd {command}。当前仅标记为 in_progress/evidence_pending；完成状态需通过证据门禁。")
    
    elif command == "report":
        sprint_banner("/tnfd report")
        print("> 生成报告前需完成 General Requirements、14 项披露建议、metrics 和 evidence index 检查。")
        print("> 若证据不足，请输出 gap report，而不是完整 TNFD 报告。")
    
    elif command in ["save", "reset"]:
        sprint_banner(f"/tnfd {command}")
        print(f"> 状态文件位置：{STATE_FILE}")
        if command == "reset":
            print("> 为避免误删用户数据，请手动确认后删除状态文件。")
    
    elif command == "help":
        help_card()
    
    else:
        print(f"⚠️ 未知指令：{command}")
        help_card()

if __name__ == "__main__":
    main()
