import sys

def solve():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    print(max(nums))

if __name__ == "__main__":
    solve()
