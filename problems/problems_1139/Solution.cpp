//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int largest1BorderedSquare(vector<vector<int>>& grid) {
		size_t m = grid.size(), n = grid[0].size();
		vector<vector<int>> pre_row(m, vector<int>(n + 1)), pre_col(m + 1, vector<int>(n));
		for (size_t i = 0; i < m; i++) {
			for (size_t j = 0; j < n; j++) {
				pre_row[i][j + 1] = pre_row[i][j] + grid[i][j];
				pre_col[i + 1][j] = pre_col[i][j] + grid[i][j];
			}
		}
		for (int d = static_cast<int>(min(m, n)); d > 0; d--) {
			for (size_t i = 0; i + d <= m; i++) {
				for (size_t j = 0; j + d <= n; j++) {
					if (pre_row[i][j + d] - pre_row[i][j] == d && pre_row[i + d - 1][j + d] - pre_row[i + d - 1][j] == d &&
						pre_col[i + d][j] - pre_col[i][j] == d && pre_col[i + d][j + d - 1] - pre_col[i][j + d - 1] == d) {
						return d * d;
					}
				}
			}
		}
		return 0;
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
	return solution.largest1BorderedSquare(grid);
}
