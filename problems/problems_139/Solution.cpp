//go:build ignore
#include "cpp/common/Solution.h"
#include <string>
#include <unordered_set>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.length();
        int max_len = ranges::max(wordDict, {}, &string::length).length();
        unordered_set words(wordDict.begin(), wordDict.end());
        vector<bool> dp(n+1);
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = i-1; j >= max(i-max_len, 0); j--) {
                if (dp[j] && words.contains(s.substr(j, i-j))) {
                    dp[i] = true;
                    break;
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
	vector<string> wordDict = json::parse(inputArray.at(1));
	return solution.wordBreak(s, wordDict);
}
