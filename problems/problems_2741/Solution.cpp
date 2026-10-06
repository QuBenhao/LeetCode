//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int specialPerm(vector<int>& nums) {
        int n = nums.size(), u = (1 << n) - 1;
        vector<vector<long long>> memo(u, vector<long long>(n, -1)); // -1 means not yet computed
        auto dfs = [&](auto&& dfs, int s, int i) -> long long {
            if (s == 0) {
                return 1; // Found a special permutation
            }
            auto& res = memo[s][i]; // This is a reference
            if (res != -1) { // Already computed
                return res;
            }
            res = 0;
            for (int j = 0; j < n; j++) {
                if ((s >> j & 1) && (nums[i] % nums[j] == 0 || nums[j] % nums[i] == 0)) {
                    res += dfs(dfs, s ^ (1 << j), j);
                }
            }
            return res;
        };
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += dfs(dfs, u ^ (1 << i), i);
        }
        return ans % 1'000'000'007;
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
	return solution.specialPerm(nums);
}
