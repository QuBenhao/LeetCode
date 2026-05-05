//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        
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
	vector<vector<string>> boxGrid_str = json::parse(inputArray.at(0));
	auto boxGrid = vector<vector<char>>(boxGrid_str.size(), vector<char>(boxGrid_str[0].size()));
	for (size_t i = 0; i < boxGrid.size(); ++i) {
		for (size_t j = 0; j < boxGrid[i].size(); ++j) {
			boxGrid[i][j] = boxGrid_str[i][j][0];
		}
	}
	return solution.rotateTheBox(boxGrid);
}
