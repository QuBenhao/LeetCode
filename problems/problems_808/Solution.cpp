//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    double soupServings(int n) {
        if (n == 0) {
			return 0.5;
		}
		n = (n + 24) / 25; // Round up to the nearest integer
		if (n >= 178) {
			return 1.0; // If n is large enough, return 1.0
		}
		vector<vector<double>> dp(n+1, vector<double>(n+1));
		dp[0][0] = 0.5; // Base case: both soups are empty
		for (int j = 1; j <= n; ++j) {
			dp[0][j] = 1.0; // If soup A is empty, all of soup B is consumed
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				dp[i][j] = 0.25 * (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][max(0, j - 1)] +
								  dp[max(0, i - 2)][max(0, j - 2)] + dp[max(0, i - 1)][max(0, j - 3)]);
			}
		}
		return dp[n][n];
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
	return solution.soupServings(n);
}
