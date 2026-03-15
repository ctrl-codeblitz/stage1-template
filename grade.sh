#!/bin/bash
set -euo pipefail

echo "== Environment =="
python3 --version
g++ --version
javac -version
java -version

echo ""
echo "== Grading =="

# Expect structure:
# solutions/<problem>/solution.py OR Main.java OR solution.cpp (or similar)
# tests/<problem>/input1.txt expected1.txt ... inputN.txt expectedN.txt

shopt -s nullglob

fail=0
total=0
passed=0
failed=0 #new variable to track failed tests

for prob_dir in solutions/*/; do
  prob_name="$(basename "$prob_dir")"
  echo ""
  echo "---- Problem: $prob_name ----"

  test_dir="tests/$prob_name"
  if [[ ! -d "$test_dir" ]]; then
    echo "ERROR: Missing test directory: $test_dir"
    fail=1
    continue
  fi

  # Pick exactly one submission file from this solutions folder.
  # Priority: .py, .java, then .cpp. (Adjust if you want different rules.)
  sub_file=""
  py_files=("$prob_dir"*.py)
  java_files=("$prob_dir"*.java)
  cpp_files=("$prob_dir"*.cpp "$prob_dir"*.cc "$prob_dir"*.cxx)

  if [[ ${#py_files[@]} -gt 0 ]]; then
    sub_file="${py_files[0]}"
  elif [[ ${#java_files[@]} -gt 0 ]]; then
    sub_file="${java_files[0]}"
  elif [[ ${#cpp_files[@]} -gt 0 ]]; then
    sub_file="${cpp_files[0]}"
  else
    echo "ERROR: No submission found in $prob_dir (expected .py, .java, or .cpp)"
    fail=1
    failed=$((failed+1)) #count for failed here
    continue
  fi

  echo "Using submission: $sub_file"

  # Run all test cases input*.txt with matching expected*.txt
  inputs=("$test_dir"/input*.txt)
  if [[ ${#inputs[@]} -eq 0 ]]; then
    echo "ERROR: No inputs found in $test_dir (expected input*.txt)"
    fail=1
    continue
  fi

  #make sure we have at least 3 test cases to be a valid test set, otherwise it's too easy to pass by chance
  MIN_TESTS=3
  if [[ ${#inputs[@]} -lt $MIN_TESTS ]]; then
    echo "ERROR: Only ${#inputs[@]} test case(s) found in $test_dir, expected at least $MIN_TESTS"
    fail=1
    continue
  fi
  #todo: maybe make chmod permissions for the tests/ folders so read-only for competitors but readable for admin

  for in_file in "${inputs[@]}"; do
    base="$(basename "$in_file")"
    suffix="${base#input}"           # e.g., "1.txt"
    exp_file="$test_dir/expected$suffix"

    if [[ ! -f "$exp_file" ]]; then
      echo "ERROR: Missing expected file for $in_file (expected $exp_file)"
      fail=1
      continue
    fi

    total=$((total+1))
    echo ""
    echo "Test: $base"

    # runner.py prints PASS/FAIL and exits 0/1 accordingly
    if python3 runner.py --file "$sub_file" --stdin "$in_file" --expected "$exp_file"; then
      passed=$((passed+1))
    else
      echo "Test FAILED: $base"
      fail=1
      failed=$((failed+1))
    fi
  done
done

echo ""
echo "== Summary =="
echo "Passed $passed / $total tests"

if [[ $fail -ne 0 ]]; then
  echo "OVERALL: FAIL"
  exit 1
else
  echo "OVERALL: PASS"
  exit 0
fi