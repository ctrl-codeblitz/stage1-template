import sys

def solve():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    
    unique_nums = sorted(list(set(nums)), reverse=True)
    if len(unique_nums) >= 2:
        print(unique_nums[1])
    # The problem statement guarantees "at least two distinct values",
    # so no need for explicit else handling for this specific problem.

if __name__ == "__main__":
    solve()
