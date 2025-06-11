//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int ans = abs(nums[0] - nums[nums.size()-1]);
        for (int i = 0; i < nums.size() - 1; ++i) {
            ans = max(ans, abs(nums[i] - nums[i + 1]));
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
	return solution.maxAdjacentDistance(nums);
}
