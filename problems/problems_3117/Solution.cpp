//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumValueSum(vector<int>& nums, vector<int>& andValues) {
        const int INF = INT_MAX / 2; // Divide by 2 to prevent overflow in + nums[i] below
        int n = nums.size(), m = andValues.size();
        unordered_map<long long, int> memo;
        auto dfs = [&](auto&& dfs, int i, int j, int and_) -> int {
            if (n - i < m - j) { // Not enough elements remain
                return INF;
            }
            if (j == m) { // Split into m segments
                return i == n ? 0 : INF;
            }
            and_ &= nums[i];
            // Pack the three parameters into one long long
            long long mask = (long long) i << 36 | (long long) j << 32 | and_;
            if (memo.contains(mask)) { // Already computed
                return memo[mask];
            }
            int res = dfs(dfs, i + 1, j, and_); // Do not split here
            if (and_ == andValues[j]) { // Split here; nums[i] is the last number in this segment
                res = min(res, dfs(dfs, i + 1, j + 1, -1) + nums[i]);
            }
            return memo[mask] = res; // Memoization
        };
        int ans = dfs(dfs, 0, 0, -1);
        return ans < INF ? ans : -1;
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
	vector<int> andValues = json::parse(inputArray.at(1));
	return solution.minimumValueSum(nums, andValues);
}
