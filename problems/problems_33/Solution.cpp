//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int search(vector<int>& nums, int target) {
		int left = 0, right = static_cast<int>(nums.size()) - 1;
		while (left < right) {
			int mid = left + (right - left) / 2;
			if (nums[mid] >= nums[0]) {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		if (target >= nums[0]) {
			right = left;
			left = 0;
		} else {
			right = static_cast<int>(nums.size()) - 1;
		}
		while (left < right) {
			int mid = left + (right - left) / 2;
			if (nums[mid] < target) {
				left = mid + 1;
			} else {
				right = mid;
			}
		}
		return nums[left] == target ? left : -1;
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
	return solution.search(nums, target);
}
