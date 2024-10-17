//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
    const int MOD = 1'000'000'007;
public:
    int numberOfPermutations(int n, vector<vector<int>>& requirements) {
        vector<int> req(n, -1);
        req[0] = 0;
        for (auto& p : requirements) {
            req[p[0]] = p[1];
        }
        if (req[0]) {
            return 0;
        }

        int m = ranges::max(req);
        vector<int> f(m + 1);
        f[0] = 1;
        for (int i = 1; i < n; i++) {
            int mx = req[i] < 0 ? m : req[i];
            if (int r = req[i - 1]; r >= 0) {
                fill(f.begin(), f.begin() + r, 0);
                fill(f.begin() + r + 1, f.begin() + min(i + r, mx) + 1, f[r]);
                fill(f.begin() + min(i + r, mx) + 1, f.end(), 0);
            } else {
                for (int j = 1; j <= mx; j++) { // 计算前缀和
                    f[j] = (f[j] + f[j - 1]) % MOD;
                }
                for (int j = mx; j > i; j--) { // 计算子数组和
                    f[j] = (f[j] - f[j - i - 1] + MOD) % MOD;
                }
            }
        }
        return f[req[n - 1]];
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
	vector<vector<int>> requirements = json::parse(inputArray.at(1));
	return solution.numberOfPermutations(n, requirements);
}
