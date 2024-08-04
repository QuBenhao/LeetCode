//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int findIntegers(int n) {
        auto dp = vector<int>(31, 0);
        dp[0] = 1;
        dp[1] = 2;
        for (int i = 2; i < 31; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        n++;
        int pre = 0, ans = 0;
        for (int i = 29; i >= 0; i--) {
            if (n & (1 << i)) {
                ans += dp[i];
                if (pre == 1) {
                    break;
                }
                pre = 1;
            } else {
                pre = 0;
            }
        }
        return ans;
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
	return solution.findIntegers(n);
}
