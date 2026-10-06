//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int countSpecialNumbers(int n) {
        string s = to_string(n);
        int m = s.length();
        vector<vector<int>> memo(m, vector<int>(1 << 10, -1)); // -1 means not yet computed
        auto dfs = [&](auto&& dfs, int i, int mask, bool is_limit, bool is_num) -> int {
            if (i == m) {
                return is_num; // is_num being true means a valid number has been formed
            }
            if (!is_limit && is_num && memo[i][mask] != -1) {
                return memo[i][mask]; // Already computed
            }
            int res = 0;
            if (!is_num) { // The current digit can be skipped
                res = dfs(dfs, i + 1, mask, false, false);
            }
            // If all previous digits match n, this digit can be at most s[i] (otherwise the number would exceed n)
            int up = is_limit ? s[i] - '0' : 9;
            // Enumerate the digit d to place
            // If no digit has been placed, start at 1 to avoid leading zeros
            for (int d = is_num ? 0 : 1; d <= up; d++) {
                if ((mask >> d & 1) == 0) { // If d is absent from mask, it has not been used before
                    res += dfs(dfs, i + 1, mask | (1 << d), is_limit && d == up, true);
                }
            }
            if (!is_limit && is_num) {
                memo[i][mask] = res; // Memoization
            }
            return res;
        };
        return dfs(dfs, 0, 0, true, false);
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
	int n = json::parse(inputArray.at(0));
	return solution.countSpecialNumbers(n);
}
