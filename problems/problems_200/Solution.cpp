//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        
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
	vector<vector<string>> grid_str = json::parse(inputArray.at(0));
	auto grid = vector<vector<char>>(grid_str.size(), vector<char>(grid_str[0].size()));
	for (int i = 0; i < grid.size(); i++) {
		for (int j = 0; j < grid[i].size(); j++) {
			grid[i][j] = grid_str[i][j][0];
		}
	}
	return solution.numIslands(grid);
}
