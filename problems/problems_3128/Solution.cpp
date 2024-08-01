//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long numberOfRightTriangles(vector<vector<int>>& grid) {
        int m = static_cast<int>(grid.size()), n = static_cast<int>(grid[0].size());
        vector<int> row_count = vector<int>(m, 0), col_count = vector<int>(n, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                row_count[i] += grid[i][j];
                col_count[j] += grid[i][j];
            }
        }
        long long ans = 0LL;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 0) {
                    ans += (static_cast<long long>(row_count[i]) - 1) * (static_cast<long long>(col_count[j]) - 1);
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
	vector<vector<int>> grid = json::parse(inputArray.at(0));
	return solution.numberOfRightTriangles(grid);
}
