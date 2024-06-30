//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int t = target;
        for (auto num: nums) {
            target += num;
        }
        if (target % 2 != 0 || target < 0 || target < 2 * t) {
            return 0;
        }
        target >>= 1;
        auto dp = vector<int>(target + 1);
        dp[0] = 1;
        for (auto num: nums) {
            for (int x = target; x >= num; x--) {
                dp[x] += dp[x - num];
            }
        }
        return dp[target];
    }
};

json leetcode::qubh::Solve(string input) {
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
	int target = json::parse(inputArray.at(1));
	return solution.findTargetSumWays(nums, target);
}
