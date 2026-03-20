#include <iostream>
#include <vector>
#include <string>
#include <sstream>

void solve() {
    // --- Input reading ---
    int n;
    std::cin >> n;
    std::vector<long long> nums(n);
    for(int i = 0; i < n; ++i) {
        std::cin >> nums[i];
    }

    // --- Solution ---
    // The following variables are available:
    // n: int
    // nums: std::vector<long long>

    // TODO: Implement the solution
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    solve();
    return 0;
}
