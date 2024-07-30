//go:build ignore
#include "cpp/common/Solution.h"
#include <random>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        auto pivot = nums[random() % nums.size()];
        vector<int> lefts, rights, equals;
        for (auto num : nums) {
            if (num < pivot) {
                lefts.push_back(num);
            } else if (num > pivot) {
                rights.push_back(num);
            } else {
                equals.push_back(num);
            }
        }
        int r = static_cast<int>(rights.size()), e = static_cast<int>(equals.size());
        if (r >= k) {
            return findKthLargest(rights, k);
        } else if (r + e >= k) {
            return pivot;
        } else {
            return findKthLargest(lefts, k - r - e);
        }
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
	return solution.findKthLargest(nums, k);
}
