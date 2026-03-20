import sys

def solve():
    lines = sys.stdin.readlines()
    n = int(lines[0])
    nums = list(map(int, lines[1].split()))
    print(sum(nums))

if __name__ == "__main__":
    solve()
