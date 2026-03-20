import sys

def solve():
    s = sys.stdin.readline().strip()
    print(s == s[::-1])

if __name__ == "__main__":
    solve()
