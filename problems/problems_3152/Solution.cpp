//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
		size_t n = nums.size();
        vector<int> pre_sum(n, 0);
		for (size_t i = 0; i + 1 < n; i++) {
			pre_sum[i + 1] = pre_sum[i] + ((nums[i] & 1) != (nums[i + 1] & 1));
		}
		vector<bool> res;
		for (auto query : queries) {
			int l = query[0], r = query[1];
			res.emplace_back(pre_sum[r] - pre_sum[l] == r - l);
		}
		return res;
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
	vector<vector<int>> queries = json::parse(inputArray.at(1));
	return solution.isArraySpecial(nums, queries);
}
