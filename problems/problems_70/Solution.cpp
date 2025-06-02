//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int climbStairs(int n) {
        int dp[3];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[i%3] = dp[(i+1)%3] + dp[(i+2)%3];
        }
        return dp[n%3];
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
	return solution.climbStairs(n);
}
