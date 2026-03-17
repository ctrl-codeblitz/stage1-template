#!/bin/bash
set -euo pipefail

STAGE_DIR="${1:-.}"

echo "== Environment =="
python3 --version
g++ --version
javac -version
java -version

echo ""
echo "== Grading Directory: $STAGE_DIR =="

# Let runner.py handle ALL the looping, missing file detection, and formatting.
# We pass --all so it runs the full 12/12 accounting.
if python3 runner.py --dir "$STAGE_DIR" --all; then
  echo "OVERALL RESULT: PASS"
  exit 0
else
  echo "OVERALL RESULT: FAIL"
  exit 1
fi