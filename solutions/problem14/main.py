import sys

def solve():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            print(f"[{num_map[complement]}, {i}]")
            return
        num_map[num] = i
    print("[]") # No solution found

if __name__ == "__main__":
    solve()
