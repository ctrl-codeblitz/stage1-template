import sys

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    
    # --- Solution ---
    # The following variables are available:
    # n: int
    # nums: list of ints
    
    # TODO: Implement the solution
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
