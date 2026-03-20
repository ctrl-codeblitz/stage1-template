import sys
from collections import Counter

def solve():
    s = sys.stdin.readline().strip()
    
    freq = Counter(s)
    
    # Output format: 'a':1, 'b':2, 'c':1
    # Sort by character for consistent output
    sorted_freq = sorted(freq.items())
    for char, count in sorted_freq:
        print(f"{char}:{count}")

if __name__ == "__main__":
    solve()
