#include <iostream>
#include <vector>
#include <string>
#include <sstream>

void solve() {
    // --- Input reading ---
    std::string line;
    std::getline(std::cin, line);
    std::stringstream ss(line);
    std::vector<int> nums;
    int num;
    while(ss >> num) {
        nums.push_back(num);
    }
    int k;
    std::cin >> k;

    // --- Solution ---
    // The following variables are available:
    // nums: std::vector<int>
    // k: int

    // TODO: Implement the solution
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    solve();
    return 0;
}
