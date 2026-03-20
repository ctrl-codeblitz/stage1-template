import sys

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    msg = sys.stdin.readline().strip()
    words_to_append = sys.stdin.readline().strip().split()
    
    # --- Solution ---
    # The following variables are available:
    # msg: str
    # words_to_append: list of strings
    
    # TODO: Implement the solution
    
  except (ValueError, IndexError):
    pass

if __name__ == "__main__":
    solve()
