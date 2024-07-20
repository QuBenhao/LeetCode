//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumMoves(vector<vector<int>>& grid) {
        vector<pair<int, int>> source, target;
        int m = static_cast<int>(grid.size()), n = static_cast<int>(grid[0].size());
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] > 1) {
                    for (int k = 0; k < grid[i][j] - 1; k++) {
                        source.emplace_back(i, j);
                    }
                } else if (grid[i][j] == 0) {
                    target.emplace_back(i, j);
                }
            }
        }
        int ans = INT_MAX;
        do {
            int total = 0;
            for (size_t i = 0; i < source.size(); i++) {
                total += abs(source[i].first - target[i].first) + abs(source[i].second - target[i].second);
            }
            ans = min(ans, total);
        } while (next_permutation(source.begin(), source.end()));
        return ans == INT_MAX ? -1 : ans;
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
	return solution.minimumMoves(grid);
}
