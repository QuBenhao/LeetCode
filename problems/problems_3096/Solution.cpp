//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumLevels(vector<int>& possible) {
        auto s = 0;
        for (auto v: possible) {
            s += v == 0 ? -1 : v;
        }
        for (auto pre = 0, i = 0; i < static_cast<int>(possible.size()) - 1; i++) {
            pre += possible[i] == 0 ? -1 : possible[i];
            if (pre * 2 > s) {
                return i + 1;
            }
        }
        return -1;
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
	vector<int> possible = json::parse(inputArray.at(0));
	return solution.minimumLevels(possible);
}
