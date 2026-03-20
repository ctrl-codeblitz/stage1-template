import sys

def solve():
    s = sys.stdin.readline().strip()
    vowels = "AEIOUaeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print(count)

if __name__ == "__main__":
    solve()
