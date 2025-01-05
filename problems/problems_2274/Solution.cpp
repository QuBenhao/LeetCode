//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxConsecutive(int bottom, int top, vector<int>& special) {
        
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
	int bottom = json::parse(inputArray.at(0));
	int top = json::parse(inputArray.at(1));
	vector<int> special = json::parse(inputArray.at(2));
	return solution.maxConsecutive(bottom, top, special);
}
