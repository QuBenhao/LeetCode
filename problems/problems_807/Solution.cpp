//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        auto n = grid.size();
        vector<int> rowMax(n, 0);
        vector<int> colMax(n, 0);
        for (size_t i = 0; i < n; i++) {
            for (size_t j = 0; j < n; j++) {
                rowMax[i] = max(rowMax[i], grid[i][j]);
                colMax[j] = max(colMax[j], grid[i][j]);
            }
        }
        int res = 0;
        for (size_t i = 0; i < n; i++) {
            for (size_t j = 0; j < n; j++) {
                res += min(rowMax[i], colMax[j]) - grid[i][j];
            }
        }
        return res;
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
	return solution.maxIncreaseKeepingSkyline(grid);
}
