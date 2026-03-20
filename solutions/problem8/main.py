import sys

def solve():
    n = int(sys.stdin.readline())
    s_n = str(n)
    digit_sum = 0
    for digit in s_n:
        digit_sum += int(digit)
    print(digit_sum)

if __name__ == "__main__":
    solve()
