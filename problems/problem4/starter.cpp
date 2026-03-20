#include <iostream>
#include <vector>
#include <string>
#include <sstream>

void solve() {
    // --- Input reading ---
    std::string msg, words_line;
    std::getline(std::cin, msg);
    std::getline(std::cin, words_line);
    
    std::stringstream ss(words_line);
    std::string word;
    std::vector<std::string> words_to_append;
    while(ss >> word) {
        words_to_append.push_back(word);
    }

    // --- Solution ---
    // The following variables are available:
    // msg: std::string
    // words_to_append: std::vector<std::string>

    // TODO: Implement the solution
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    solve();
    return 0;
}
