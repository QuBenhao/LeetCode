//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
private:
    int DivCon(vector<int>& nums, int left, int right) {
        if (left == right) {
            return nums[left];
        }
        int mid = left + (right - left) / 2;
        int left_sum = DivCon(nums, left, mid);
        int right_sum = DivCon(nums, mid + 1, right);
        int cross_sum = 0, left_cross_sum = nums[mid], right_cross_sum = 0;
        for (int i = mid; i >= left; i--) {
            cross_sum += nums[i];
            left_cross_sum = max(cross_sum, left_cross_sum);
        }
        cross_sum = 0;
        for (int i = mid + 1; i <= right; i++) {
            cross_sum += nums[i];
            right_cross_sum = max(cross_sum, right_cross_sum);
        }
        return max(max(left_sum, right_sum), left_cross_sum + right_cross_sum);
    }
public:
    int maxSubArray(vector<int>& nums) {
        return DivCon(nums, 0, static_cast<int>(nums.size()) - 1);
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
	return solution.maxSubArray(nums);
}
