//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
private:
    void backtrack(vector<vector<int>>& res, vector<int>& nums, int idx) {
        if (idx == static_cast<int>(nums.size())) {
            res.push_back(nums);
            return;
        }
        for (int i = idx; i < static_cast<int>(nums.size()); i++) {
            swap(nums[i], nums[idx]);
            backtrack(res, nums, idx + 1);
            swap(nums[i], nums[idx]);
        }
    }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        backtrack(res, nums, 0);
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
	return solution.permute(nums);
}
