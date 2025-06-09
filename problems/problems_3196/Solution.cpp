//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long maximumTotalCost(vector<int>& nums) {
        int n = nums.size();
		long long f0 = nums[0], f1 = nums[0];
		for (int i = 1; i < n; ++i) {
			long long f2 = f1 - nums[i];
			f1 = max(f0, f1) + nums[i];
			f0 = f2;
		}
		return max(f0, f1);
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
	return solution.maximumTotalCost(nums);
}
