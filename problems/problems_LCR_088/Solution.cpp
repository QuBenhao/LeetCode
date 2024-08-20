//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
		int n = static_cast<int>(cost.size());
		vector<int> dp(3, 0);
		for (int i = 2; i <= n; i++) {
			dp[i % 3] = min(dp[(i - 1) % 3] + cost[i - 1], dp[(i - 2) % 3] + cost[i - 2]);
		}
		return dp[n % 3];
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
	vector<int> cost = json::parse(inputArray.at(0));
	return solution.minCostClimbingStairs(cost);
}
