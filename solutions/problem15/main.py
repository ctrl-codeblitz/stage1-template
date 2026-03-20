import sys
from collections import Counter

def solve():
    s1, s2 = sys.stdin.readline().split()
    print(Counter(s1) == Counter(s2))

if __name__ == "__main__":
    solve()
