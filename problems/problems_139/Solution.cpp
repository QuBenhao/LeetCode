//go:build ignore
#include "cpp/common/Solution.h"
#include <string>
#include <unordered_set>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
		unordered_set<string> words;
		for (const string& word : wordDict) {
			words.insert(word);
		}
		int n = static_cast<int>(s.size());
		vector<bool> dp(n + 1, false);
		dp[0] = true;
		for (int i = 1; i <= n; i++) {
			for (int j = 0; j < i; j++) {
				if (dp[j] && words.find(s.substr(j, i - j)) != words.end()) {
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
