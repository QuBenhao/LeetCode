//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int incremovableSubarrayCount(vector<int>& nums) {
        int n = static_cast<int>(nums.size());
        auto i = 0;
        while (i < n - 1 && nums[i] < nums[i + 1]) {
            i++;
        }
        if (i == n - 1) {
            return n * (n + 1) / 2;
        }
        auto ans = i + 2;
        auto j = n - 1;
        while (j == n - 1 || nums[j] < nums[j + 1]) {
            while (i >= 0 && nums[i] >= nums[j]) {
                i--;
            }
            ans += i + 2;
            j--;
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
	return solution.incremovableSubarrayCount(nums);
}
