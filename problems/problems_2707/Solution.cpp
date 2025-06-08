//go:build ignore
#include "cpp/common/Solution.h"

#include <unordered_set>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        unordered_set<string> cache(dictionary.begin(), dictionary.end());
        int n = s.size();
        vector<int> dp(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            dp[i + 1] = dp[i] + 1; // Assume the worst case: every character is an extra character
            for (int j = 0; j <= i; ++j) {
                string sub = s.substr(j, i - j + 1);
                if (cache.find(sub) != cache.end()) {
                    dp[i + 1] = min(dp[i + 1], dp[j]); // If the substring is in the dictionary, no extra character needed
                }
            }
        }
        return dp[n];
    }
};

json leetcode::qubh::Solve(string input_json_values) {
	vector<string> inputArray;
	size_t pos = input_json_values.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input_json_values.substr(0, pos));
		input_json_values = input_json_values.substr(pos + 1);
		pos = input_json_values.find('\n');
	}
	inputArray.push_back(input_json_values);

	Solution solution;
	string s = json::parse(inputArray.at(0));
	vector<string> dictionary = json::parse(inputArray.at(1));
	return solution.minExtraChar(s, dictionary);
}
