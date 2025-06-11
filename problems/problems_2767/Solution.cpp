//go:build ignore
#include "cpp/common/Solution.h"

#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumBeautifulSubstrings(string s) {
        auto isFivePow = [](int num) -> bool {
            if (num == 0) return false;
            while (num > 1) {
                if (num % 5 != 0) return false;
                num /= 5;
            }
            return num == 1;
        };
        int n = s.size();
        vector<int> preSum(n+1, 0);
        for (int i = 0; i < n; ++i) {
            preSum[i + 1] = (preSum[i] << 1) + (s[i] - '0');
        }
        vector<int> dp(n + 1, n + 1);
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j <= i; ++j) {
                if (s[j] == '0') continue;
                int cur = preSum[i+1]^(preSum[j] << (i - j + 1));
                if (isFivePow(cur)) {
                    dp[i + 1] = min(dp[i + 1], dp[j] + 1);
                }
            }
        }
        return dp[n] == n + 1 ? -1 : dp[n];
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
	string s = json::parse(inputArray.at(0));
	return solution.minimumBeautifulSubstrings(s);
}
