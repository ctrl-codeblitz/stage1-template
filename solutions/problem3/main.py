import sys

def solve():
    s = sys.stdin.readline()
    open_count = s.count('(')
    close_count = s.count(')')
    print(open_count == close_count)

if __name__ == "__main__":
    solve()
