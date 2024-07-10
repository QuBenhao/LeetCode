//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        auto ans = vector<vector<int>>(numRows);
        for (auto i = 0; i < numRows; i++) {
            ans[i] = vector<int>(i + 1, 1);
            for (auto j = 1; j < i / 2 + 1; j++) {
                ans[i][j] = ans[i][i - j] = ans[i - 1][j - 1] + ans[i - 1][j];
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
	int numRows = json::parse(inputArray.at(0));
	return solution.generate(numRows);
}
