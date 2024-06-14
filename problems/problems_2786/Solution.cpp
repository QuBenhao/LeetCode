//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long maxScore(vector<int>& nums, int x) {
        long long ans = nums[0];
        vector<long long> dp = {INT_MIN, INT_MIN};
        dp[nums[0] % 2] = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            int idx = nums[i] % 2;
            long long cur = max(dp[idx] + nums[i], dp[idx ^ 1] + nums[i] - x);
            ans = max(ans, cur);
            dp[idx] = max(dp[idx], cur);
        }
        return ans;
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
	int x = json::parse(inputArray.at(1));
	return solution.maxScore(nums, x);
}
