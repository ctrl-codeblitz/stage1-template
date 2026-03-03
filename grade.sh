#!/bin/bash

any_failure=0

for i in solutions/*/
do
    problem=$(basename $i)
    
    # Find the solution file and determine language
    if [ -f "solutions/$problem/solution.py" ]; then
        lang="python"
        solution_file="solutions/$problem/solution.py"
    elif [ -f "solutions/$problem/solution.java" ]; then
        lang="java"
        solution_file="solutions/$problem/solution.java"
    elif [ -f "solutions/$problem/solution.cpp" ]; then
        lang="cpp"
        solution_file="solutions/$problem/solution.cpp"
    else
        echo "$problem: No solution file found"
        any_failure=1
        continue
    fi
    
    # Compile if needed
    if [ "$lang" = "java" ]; then
        javac $solution_file
        if [ $? -ne 0 ]; then
            echo "$problem: Compilation failed"
            any_failure=1
            continue
        fi
    elif [ "$lang" = "cpp" ]; then
        g++ $solution_file -o solutions/$problem/solution
        if [ $? -ne 0 ]; then
            echo "$problem: Compilation failed"
            any_failure=1
            continue
        fi
    fi
    
    for test_input in tests/$problem/input*.txt
    do
        # Extract the test number from the filename
        test_num=$(basename $test_input | grep -o '[0-9]\+')
        
        # Run the solution based on language with timeout
        if [ "$lang" = "python" ]; then
            result=$(timeout 10 python3 $solution_file < $test_input)
        elif [ "$lang" = "java" ]; then
            result=$(cd solutions/$problem && timeout 10 java solution < ../../$test_input)
        elif [ "$lang" = "cpp" ]; then
            result=$(timeout 10 solutions/$problem/solution < $test_input)
        fi
        
        # Check if timeout occurred
        if [ $? -eq 124 ]; then
            echo "$problem test $test_num: TIMEOUT"
            any_failure=1
            continue
        fi
        
        # Read the expected output
        expected=$(cat tests/$problem/expected$test_num.txt)
        
        # Compare them
        if [ "$result" = "$expected" ]; then
            echo "$problem test $test_num: PASS"
        else
            echo "$problem test $test_num: FAIL"
            any_failure=1
        fi
    done
done

# Exit with failure if any test failed
exit $any_failure
