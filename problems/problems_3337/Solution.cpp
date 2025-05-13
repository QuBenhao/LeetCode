//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int lengthAfterTransformations(string s, int t, vector<int>& nums) {
        
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
	string s = json::parse(inputArray.at(0));
	int t = json::parse(inputArray.at(1));
	vector<int> nums = json::parse(inputArray.at(2));
	return solution.lengthAfterTransformations(s, t, nums);
}
