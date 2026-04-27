#!/bin/bash
# TNFD-disclosure Smoke Test
# Runs basic sanity checks on the skill's Python scripts
# Exit 0 = all pass, non-zero = failure

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

echo "=== TNFD-disclosure Smoke Test ==="
echo ""

pushd "$SKILL_DIR" > /dev/null

# Test 1: process_encore_data.py
echo "[1/4] python3 scripts/process_encore_data.py ..."
python3 scripts/process_encore_data.py
echo "      PASS"
echo ""

# Test 2: tnfd_handler.py /tnfd
echo "[2/4] python3 scripts/tnfd_handler.py /tnfd ..."
python3 scripts/tnfd_handler.py /tnfd > /dev/null
echo "      PASS"
echo ""

# Test 3: tnfd_handler.py /tnfd status
echo "[3/4] python3 scripts/tnfd_handler.py /tnfd status ..."
python3 scripts/tnfd_handler.py /tnfd status > /dev/null
echo "      PASS"
echo ""

# Test 4: tnfd_handler.py /tnfd kpi
echo "[4/4] python3 scripts/tnfd_handler.py /tnfd kpi ..."
python3 scripts/tnfd_handler.py /tnfd kpi > /dev/null
echo "      PASS"
echo ""

popd > /dev/null

echo "=== All 4 tests passed ==="
exit 0
