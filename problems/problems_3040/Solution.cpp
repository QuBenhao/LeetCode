//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxOperations(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> memo(n, vector<int>(n));
        bool done = false;
        auto helper = [&](int i, int j, int target) -> int {
            if (done) return 0;
            for (auto& row : memo) {
                ranges::fill(row, -1); // -1 means not yet computed
            }
            function<int(int, int)> dfs = [&](int i, int j) -> int {
                if (done) return 0;
                if (i >= j) {
                    done = true;
                    return 0;
                }
                int& res = memo[i][j]; // This is a reference
                if (res != -1) return res; // Already computed
                res = 0;
                if (nums[i] + nums[i + 1] == target) res = max(res, dfs(i + 2, j) + 1);
                if (nums[j - 1] + nums[j] == target) res = max(res, dfs(i, j - 2) + 1);
                if (nums[i] + nums[j] == target) res = max(res, dfs(i + 1, j - 1) + 1);
                return res;
            };
            return dfs(i, j);
        };
        int res1 = helper(2, n - 1, nums[0] + nums[1]); // Remove the first two numbers
        int res2 = helper(0, n - 3, nums[n - 2] + nums[n - 1]); // Remove the last two numbers
        int res3 = helper(1, n - 2, nums[0] + nums[n - 1]); // Remove the first and last numbers
        return max({res1, res2, res3}) + 1; // Include the first operation
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
