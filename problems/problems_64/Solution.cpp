//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        auto m = grid.size(), n = grid[0].size();
        vector<int> dp(n, 0);
        for (size_t i = 0; i < m; i++) {
            dp[0] += grid[i][0];
            for (size_t j = 1; j < n; j++) {
                dp[j] = (i == 0 ? dp[j - 1] : min(dp[j], dp[j - 1])) + grid[i][j];
            }
        }
        return dp[n - 1];
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
	vector<vector<int>> grid = json::parse(inputArray.at(0));
	return solution.minPathSum(grid);
}
