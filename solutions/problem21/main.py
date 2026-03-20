import sys

def solve():
    nums = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    
    n = len(nums)
    k = k % n # Handle k larger than n
    
    # Perform rotation
    rotated_nums = nums[-k:] + nums[:-k]
    print(rotated_nums)

if __name__ == "__main__":
    solve()
