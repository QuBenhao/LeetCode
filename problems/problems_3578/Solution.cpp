//go:build ignore
#include "cpp/common/Solution.h"

#include <deque>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
    const int MOD = 1e9 + 7;
public:
    int countPartitions(vector<int>& nums, int k) {
        int n = nums.size();

        deque<int> min_queue;
        deque<int> max_queue;

        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        int sum_f = 0;
        int left = 0;

        for (int i = 0; i < n; ++i) {
            sum_f = (sum_f + dp[i]) % MOD;

            while (!min_queue.empty() && nums[min_queue.back()] >= nums[i]) {
                min_queue.pop_back();
            }
            min_queue.push_back(i);

            while (!max_queue.empty() && nums[max_queue.back()] <= nums[i]) {
                max_queue.pop_back();
            }
            max_queue.push_back(i);

            while (nums[max_queue.front()] - nums[min_queue.front()] > k) {
                sum_f = (sum_f - dp[left] + MOD) % MOD;
                ++left;
                if (min_queue.front() < left) {
                    min_queue.pop_front();
                }
                if (max_queue.front() < left) {
                    max_queue.pop_front();
                }
            }
            dp[i + 1] = sum_f;
        }
        return dp[n];
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
	return solution.countPartitions(nums, k);
}
