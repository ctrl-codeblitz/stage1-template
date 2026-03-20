import sys
import json

def solve():
    accounts = json.loads(sys.stdin.read())
    
    max_sum = float('-inf')
    for row in accounts:
        current_sum = sum(row)
        if current_sum > max_sum:
            max_sum = current_sum
    print(max_sum)

if __name__ == "__main__":
    solve()
