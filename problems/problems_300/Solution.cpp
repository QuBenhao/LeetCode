//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
		vector<int> stack;
		for (int num : nums) {
			if (stack.empty() || num > stack.back()) {
				stack.push_back(num);
			} else {
				int left = 0, right = static_cast<int>(stack.size()) - 1;
				while (left < right) {
					int mid = left + (right - left) / 2;
					if (stack[mid] < num) {
						left = mid + 1;
					} else {
						right = mid;
					}
				}
				stack[right] = num;
			}
		}
		return static_cast<int>(stack.size());
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
