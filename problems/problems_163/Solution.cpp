//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<vector<int>> findMissingRanges(vector<int>& nums, int lower, int upper) {
        
    }
};

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<int> nums = json::parse(inputArray.at(0));
	int lower = json::parse(inputArray.at(1));
	int upper = json::parse(inputArray.at(2));
	return solution.findMissingRanges(nums, lower, upper);
}
