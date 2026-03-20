#include <iostream>
#include <vector>
#include <string>
#include <sstream>

void solve() {
    // --- Input reading ---
    std::string line1, line2;
    std::getline(std::cin, line1);
    std::getline(std::cin, line2);
    
    std::stringstream ss1(line1);
    std::vector<int> a;
    int n;
    while(ss1 >> n) {
        a.push_back(n);
    }
    
    std::stringstream ss2(line2);
    std::vector<int> b;
    while(ss2 >> n) {
        b.push_back(n);
    }

    // --- Solution ---
    // The following variables are available:
    // a: std::vector<int>
    // b: std::vector<int>

    // TODO: Implement the solution
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    solve();
    return 0;
}
