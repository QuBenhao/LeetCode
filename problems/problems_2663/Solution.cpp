//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string smallestBeautifulString(string s, int k) {
        k += 'a';
        int n = s.length();
        int i = n - 1; // Start with the last letter
        s[i]++; // Increment first
        while (i < n) {
            if (s[i] == k) { // A carry is needed
                if (i == 0) { // Cannot carry
                    return "";
                }
                // Carry
                s[i] = 'a';
                s[--i]++;
            } else if (i && s[i] == s[i - 1] || i > 1 && s[i] == s[i - 2]) {
                s[i]++; // If s[i] forms a palindrome with characters to its left, keep incrementing s[i]
            } else {
                i++; // Move forward to check for palindromes in the suffix
            }
        }
        return s;
    }
};

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	string s = json::parse(inputArray.at(0));
	int k = json::parse(inputArray.at(1));
	return solution.smallestBeautifulString(s, k);
}
