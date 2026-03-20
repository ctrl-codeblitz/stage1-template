import sys
import math

def solve():
    a, b = map(int, sys.stdin.readline().split())
    print(math.gcd(a, b))

if __name__ == "__main__":
    solve()
