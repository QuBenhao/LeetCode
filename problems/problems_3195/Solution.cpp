//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumArea(const vector<vector<int>>& grid) {
			int m = grid.size(), n = grid[0].size();
      int left = n, right = -1, top = m, bottom = -1;
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					if (grid[i][j] == 1) {
						left = min(left, j);
						right = max(right, j);
						top = min(top, i);
						bottom = max(bottom, i);
					}
				}
			}
			return (right - left + 1) * (bottom - top + 1);
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
	return solution.minimumArea(grid);
}
