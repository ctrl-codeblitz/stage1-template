#!/bin/bash

for i in solutions/*/
do
    problem=$(basename $i)
    for test_input in tests/$problem/input*.txt
    do
        # Extract the test number from the filename (e.g., "input1.txt" -> "1")
        test_num=$(basename $test_input | grep -o '[0-9]\+')
        
        # Run the solution and capture output
        result=$(python3 solutions/$problem/solution.py < $test_input)
        
        # Read the expected output
        expected=$(cat tests/$problem/expected$test_num.txt)
        
        # Compare them
        if [ "$result" = "$expected" ]; then
            echo "$problem test $test_num: PASS"
        else
            echo "$problem test $test_num: FAIL"
        fi
    done
done
