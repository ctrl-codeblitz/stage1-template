import sys
import json

def solve():
  """
  Reads input from stdin, solves the problem, and prints the output.
  """
  try:
    # --- Input reading ---
    # The input is a string representation of a 2D integer array.
    # Example: [[1,2,3],[3,2,1]]
    accounts = json.loads(sys.stdin.read())
    
    # --- Solution ---
    # The following variables are available:
    # accounts: list of lists of ints (e.g., [[1,2,3],[3,2,1]])
    
    # TODO: Implement the solution
    
  except (ValueError, json.JSONDecodeError):
    # Handle potential errors during JSON parsing or if input is not valid
    pass

if __name__ == "__main__":
    solve()