import sys

def solve():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    print(*result) # Print space-separated

if __name__ == "__main__":
    solve()
