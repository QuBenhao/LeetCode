//go:build ignore
#include "cpp/common/Solution.h"

#include <unordered_set>

using namespace std;
using json = nlohmann::json;

class Solution {
	int hash(int a, int b) {
		return a << 14 | b;
	}
public:
    bool sequenceReconstruction(vector<int>& nums, vector<vector<int>>& sequences) {
		unordered_set<int> pairs;
		for (const auto& seq : sequences) {
			for (size_t i = 0; i < seq.size() - 1; ++i) {
				pairs.insert(hash(seq[i], seq[i + 1]));
			}
		}
		for (size_t i = 0; i < nums.size() - 1; ++i) {
			if (pairs.find(hash(nums[i], nums[i + 1])) == pairs.end()) {
				return false;
			}
		}
		return true;
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
	vector<int> nums = json::parse(inputArray.at(0));
	vector<vector<int>> sequences = json::parse(inputArray.at(1));
	return solution.sequenceReconstruction(nums, sequences);
}
