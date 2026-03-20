#include <iostream>
#include <vector>
#include <string>
#include <sstream> // For stringstream if needed for parsing

void solve() {
    // --- Input reading ---
    // The input is a string representation of a 2D integer array.
    // Example: [[1,2,3],[3,2,1]]
    // Parsing this format in C++ requires manual string manipulation.
    std::string input_line;
    std::getline(std::cin, input_line);

    // --- Solution ---
    // The following variables are available:
    // input_line: std::string (e.g., "[[1,2,3],[3,2,1]]")
    // You will need to parse this string into a 2D vector of integers.

    // TODO: Implement the solution, including parsing input_line
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    solve();
    return 0;
}