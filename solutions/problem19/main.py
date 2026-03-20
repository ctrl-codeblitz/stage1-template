import sys

def solve():
    nums = list(map(int, sys.stdin.readline().split()))
    
    squared_nums = [x * x for x in nums]
    squared_nums.sort()
    print(squared_nums)

if __name__ == "__main__":
    solve()
