//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool canJump(vector<int>& nums) {
		int max_dis = 0, n = static_cast<int>(nums.size());
		for (int i = 0; i < n; i++) {
			max_dis = max(max_dis, i + nums[i]);
			if (max_dis >= n - 1) {
				return true;
			}
			if (i >= max_dis) {
				return false;
			}
		}
		return false;
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
	return solution.canJump(nums);
}
