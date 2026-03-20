import sys
import math

def solve():
    n = int(sys.stdin.readline())

    if n < 2:
        print("Not prime")
        return
    
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("Prime")
    else:
        print("Not prime")

if __name__ == "__main__":
    solve()
