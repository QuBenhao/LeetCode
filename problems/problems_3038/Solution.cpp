//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxOperations(vector<int>& nums) {
        for (int i = 2, s = nums[0] + nums[1]; i < nums.size() - 1; i += 2) {
            if (nums[i] + nums[i + 1] != s) {
                return i / 2;
            }
        }
        return int(nums.size()) / 2;
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
	return solution.maxOperations(nums);
}
