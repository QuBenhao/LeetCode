//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<vector<int>> modifiedMatrix(vector<vector<int>>& matrix) {
        auto m = matrix.size(), n = matrix[0].size();
        for (size_t j = 0; j < n; j++) {
            auto mx = -1;
            auto remain = vector<size_t>();
            for (size_t i = 0; i < m; i++) {
                if (matrix[i][j] != -1) {
                    mx = max(mx, matrix[i][j]);
                } else {
                    remain.push_back(i);
                }
            }
            for (auto i: remain) {
                matrix[i][j] = mx;
            }
        }
        return matrix;
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
	vector<vector<int>> matrix = json::parse(inputArray.at(0));
	return solution.modifiedMatrix(matrix);
}
