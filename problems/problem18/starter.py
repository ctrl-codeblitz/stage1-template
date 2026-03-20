import sys

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    list_a = list(map(int, sys.stdin.readline().split()))
    list_b = list(map(int, sys.stdin.readline().split()))
    
    # --- Solution ---
    # The following variables are available:
    # list_a: list of ints
    # list_b: list of ints
    
    # TODO: Implement the solution
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
