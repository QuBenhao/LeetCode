//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        
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
	vector<vector<string>> matrix_str = json::parse(inputArray.at(0));
	auto matrix = vector<vector<char>>(matrix_str.size(), vector<char>(matrix_str[0].size()));
	for (size_t i = 0; i < matrix.size(); ++i) {
		for (size_t j = 0; j < matrix[i].size(); ++j) {
			matrix[i][j] = matrix_str[i][j][0];
		}
	}
	return solution.maximalRectangle(matrix);
}
