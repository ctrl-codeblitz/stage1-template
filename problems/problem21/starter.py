import sys

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    nums = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    
    # --- Solution ---
    # The following variables are available:
    # nums: list of ints
    # k: int
    
    # TODO: Implement the solution
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
