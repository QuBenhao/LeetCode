//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int rob(vector<int>& nums) {
        auto dp0 = 0, dp1 = nums[0];
        for (size_t i = 1; i < nums.size(); i++) {
            auto dp2 = max(dp0 + nums[i], dp1);
            dp0 = max(dp0, dp1);
            dp1 = dp2;
        }
        return max(dp0, dp1);
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
	return solution.rob(nums);
}
