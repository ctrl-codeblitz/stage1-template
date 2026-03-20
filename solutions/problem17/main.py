import sys

def solve():
    nums = list(map(int, sys.stdin.readline().split()))
    
    n = len(nums)
    # Sum of numbers from 0 to n is n*(n+1)/2
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    
    print(expected_sum - actual_sum)

if __name__ == "__main__":
    solve()
