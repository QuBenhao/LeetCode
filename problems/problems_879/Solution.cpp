//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
	const int MOD = 1e9 + 7;
public:
    int profitableSchemes(int n, int minProfit, vector<int>& group, vector<int>& profit) {
	  vector<vector<int>> dp(n + 1, vector<int>(minProfit + 1, 0));
	  dp[0][0] = 1; // Base case: 1 way to achieve 0 profit with 0 members
	  int ans = minProfit == 0 ? 1 : 0; // If minProfit is 0, count the empty scheme
	  for (int i = 0; i < group.size(); ++i) {
		int g = group[i], p = profit[i];
		for (int j = n-g; j >= 0; --j) {
			for (int k = minProfit; k >= 0; --k) {
				int newProfit = min(k + p, minProfit);
				dp[j + g][newProfit] = (dp[j + g][newProfit] + dp[j][k]) % MOD;
				if (newProfit >= minProfit) {
					ans = (ans + dp[j][k]) % MOD; // Count schemes that meet or exceed minProfit
				}
			}
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
	int n = json::parse(inputArray.at(0));
	int minProfit = json::parse(inputArray.at(1));
	vector<int> group = json::parse(inputArray.at(2));
	vector<int> profit = json::parse(inputArray.at(3));
	return solution.profitableSchemes(n, minProfit, group, profit);
}
