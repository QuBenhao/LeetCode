//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int left = 0, idx = 0; idx < nums.size(); idx++) {
            if (nums[idx] != 0) {
                swap(nums[left++], nums[idx]);
            }
        }
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<int> nums = json::parse(inputArray.at(0));
    solution.moveZeroes(nums);
	return nums;
}
