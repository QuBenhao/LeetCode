//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int smallestRangeII(vector<int>& nums, int k) {
        ranges::sort(nums);
        int ans = nums.back() - nums[0];
        for (int i = 1; i < nums.size(); i++) {
            int mx = max(nums[i - 1] + k, nums.back() - k);
            int mn = min(nums[0] + k, nums[i] - k);
            ans = min(ans, mx - mn);
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
	vector<int> nums = json::parse(inputArray.at(0));
	int k = json::parse(inputArray.at(1));
	return solution.smallestRangeII(nums, k);
}
