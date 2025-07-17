//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumLength(const vector<int>& nums, int k) {
      vector<vector<int>> dp(k, vector<int>(k));
			int ans = 0;
			for (int num: nums) {
				num %= k;
				for (int i = 0; i < k; ++i) {
					dp[num][i] = dp[i][num] + 1;
					ans = max(ans, dp[num][i]);
				}
			}
			return ans;
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
	vector<int> nums = json::parse(inputArray.at(0));
	int k = json::parse(inputArray.at(1));
	return solution.maximumLength(nums, k);
}
