import sys

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    a, b = map(int, sys.stdin.read().split())
    
    # --- Solution ---
    # The following variables are available:
    # a: int
    # b: int
    
    # TODO: Implement the solution
    
  except ValueError:
    # It's good practice to handle potential errors, but for this problem,
    # the input is guaranteed to be valid integers.
    pass

if __name__ == "__main__":
    solve()
