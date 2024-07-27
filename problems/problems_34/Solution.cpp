//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto bisectLeft = [&](int target) -> int {
            int left = 0, right = static_cast<int>(nums.size());
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (nums[mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            return left;
        };
        auto bisectRight = [&](int target) -> int {
            int left = 0, right = static_cast<int>(nums.size());
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (nums[mid] <= target) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            return left;
        };
        int left = bisectLeft(target);
        int right = bisectRight(target) - 1;
        if (left <= right && nums[left] == target && nums[right] == target) {
            return {left, right};
        }
        return {-1, -1};
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
	int target = json::parse(inputArray.at(1));
	return solution.searchRange(nums, target);
}
