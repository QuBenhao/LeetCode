//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
		auto m = nums1.size(), n = nums2.size();
		vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
		for (size_t i = 1; i <= m; i++) {
			for (size_t j = 1; j <= n; j++) {
				if (nums1[i - 1] == nums2[j - 1]) {
					dp[i][j] = dp[i - 1][j - 1] + 1;
				} else {
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
				}
			}
		}
		return dp[m][n];
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
	vector<int> nums1 = json::parse(inputArray.at(0));
	vector<int> nums2 = json::parse(inputArray.at(1));
	return solution.maxUncrossedLines(nums1, nums2);
}
