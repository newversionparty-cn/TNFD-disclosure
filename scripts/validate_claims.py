#!/usr/bin/env python3
"""
Validate that high-risk pending claims are not used as verified facts in active skill files.

Default scan scope is intentionally limited to files that are loaded or shown frequently:
SKILL.md, README files, QUICK_REFERENCE, and prompts. Use --all to scan all markdown files.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
REGISTRY_FILE = SKILL_DIR / "data" / "case_claims_verification.json"
DEFAULT_PATHS = [
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "README.md",
    SKILL_DIR / "README_en.md",
    SKILL_DIR / "QUICK_REFERENCE.md",
    *sorted((SKILL_DIR / "prompts").glob("*.md")),
]

SAFE_MARKERS = [
    "待核验",
    "pending",
    "unverified",
    "verification_status",
    "claim registry",
    "registry",
    "不得作为确定事实",
    "不能作为确定事实",
]


def load_pending_claims() -> list[dict]:
    with REGISTRY_FILE.open(encoding="utf-8") as f:
        registry = json.load(f)
    return [
        claim
        for claim in registry.get("claims", [])
        if claim.get("verification_status") == "pending"
    ]


def risky_terms(claim: dict) -> set[str]:
    terms: set[str] = set()
    company = str(claim.get("company", ""))
    if company and company not in {"TNFD", "Industry Benchmark"}:
        terms.add(company)
        if "(" in company:
            terms.add(company.split("(")[0].strip())

    text = " ".join(str(claim.get(k, "")) for k in ("claim_zh", "claim_en"))
    for token in re.findall(r"\d+(?:\.\d+)?/14|\d+(?:\.\d+)?%|\d+(?:\.\d+)? 万元|\d+-\d+ 万元|416\+", text):
        if token.strip():
            terms.add(token.strip())
    if "50-200" in text:
        terms.add("50-200")
    return {term for term in terms if len(term) >= 3}


def line_is_safe(line: str) -> bool:
    lowered = line.lower()
    return any(marker.lower() in lowered for marker in SAFE_MARKERS)


def scan_file(path: Path, pending_claims: list[dict]) -> list[str]:
    if not path.exists():
        return []
    findings: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    for idx, line in enumerate(lines, start=1):
        if line_is_safe(line):
            continue
        for claim in pending_claims:
            matched_terms = [term for term in risky_terms(claim) if term in line]
            if matched_terms:
                findings.append(
                    f"{path.relative_to(SKILL_DIR)}:{idx}: pending claim used without marker "
                    f"({claim.get('id')}): {', '.join(matched_terms[:3])}"
                )
                break
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="scan all markdown files")
    args = parser.parse_args()

    pending_claims = load_pending_claims()
    paths = sorted(SKILL_DIR.rglob("*.md")) if args.all else DEFAULT_PATHS

    findings: list[str] = []
    for path in paths:
        findings.extend(scan_file(path, pending_claims))

    if findings:
        print("Claim validation failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print(f"Claim validation passed for {len(paths)} active files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
