//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>
#include <algorithm>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp;
        for (auto num: nums) {
            auto it = lower_bound(dp.begin(), dp.end(), num);
            if (it == dp.end()) {
                dp.push_back(num);
            } else {
                *it = num;
            }
        }
        return dp.size();
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
	return solution.lengthOfLIS(nums);
}
