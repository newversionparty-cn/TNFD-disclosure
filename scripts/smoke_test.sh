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
TMP_TNFD_HOME="$(mktemp -d)"
cleanup() {
  rm -rf "$TMP_TNFD_HOME"
  rm -rf "$SKILL_DIR/.tnfd"
  rm -rf "$SKILL_DIR/outputs"
}
trap cleanup EXIT

export TNFD_HOME="$TMP_TNFD_HOME"

echo "[1/7] python3 scripts/process_encore_data.py ..."
python3 scripts/process_encore_data.py
echo "      PASS"
echo ""

# Test 2: tnfd_handler.py /tnfd
echo "[2/7] python3 scripts/tnfd_handler.py /tnfd ..."
python3 scripts/tnfd_handler.py /tnfd > /dev/null
echo "      PASS"
echo ""

# Test 3: beginner start
echo "[3/7] python3 scripts/tnfd_handler.py /tnfd start ..."
python3 scripts/tnfd_handler.py /tnfd start > /dev/null
echo "      PASS"
echo ""

# Test 4: create project
echo "[4/7] python3 scripts/tnfd_handler.py /tnfd new Demo Solar ..."
python3 scripts/tnfd_handler.py /tnfd new Demo Solar > /dev/null
echo "      PASS"
echo ""

# Test 5: tnfd_handler.py /tnfd status
echo "[5/7] python3 scripts/tnfd_handler.py /tnfd status ..."
python3 scripts/tnfd_handler.py /tnfd status > /dev/null
echo "      PASS"
echo ""

# Test 6: tnfd_handler.py /tnfd kpi
echo "[6/7] python3 scripts/tnfd_handler.py /tnfd kpi ..."
python3 scripts/tnfd_handler.py /tnfd kpi > /dev/null
echo "      PASS"
echo ""

# Test 7: export artifacts
echo "[7/7] python3 scripts/tnfd_handler.py /tnfd export all ..."
python3 scripts/tnfd_handler.py /tnfd export all > /dev/null
test -f "$SKILL_DIR/outputs/tnfd_lea/TNFD_LEA_Workbook.xlsx"
test -f "$SKILL_DIR/outputs/tnfd_lea/TNFD_LEA_Preliminary_Report.md"
echo "      PASS"
echo ""

popd > /dev/null

echo "=== All 7 tests passed ==="
exit 0
