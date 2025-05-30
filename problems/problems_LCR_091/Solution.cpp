//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int dp[2][3]{};
        int n = costs.size();
        for (int i = 0; i < n; i++) {
            int cur = i%2, pre = (i+1)%2;
            dp[cur][0] = min(dp[pre][1], dp[pre][2]) + costs[i][0];
            dp[cur][1] = min(dp[pre][0], dp[pre][2]) + costs[i][1];
            dp[cur][2] = min(dp[pre][1], dp[pre][0]) + costs[i][2];
        }
        int last = (n+1)%2;
        return min(min(dp[last][0], dp[last][1]), dp[last][2]);
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
	vector<vector<int>> costs = json::parse(inputArray.at(0));
	return solution.minCost(costs);
}
