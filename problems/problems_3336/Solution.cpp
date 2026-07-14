//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int subsequencePairCount(vector<int>& nums) {
        const int MOD = 1000000007;
        const int N = 201;
        vector<long long> dp(N * N, 0);
        dp[0] = 1;
        for (int x : nums) {
            vector<long long> ndp = dp;
            for (int ga = 0; ga < N; ++ga) {
                for (int gb = 0; gb < N; ++gb) {
                    long long c = dp[ga * N + gb];
                    if (c == 0) continue;
                    int nga = std::gcd(ga, x);
                    ndp[nga * N + gb] = (ndp[nga * N + gb] + c) % MOD;
                    int ngb = std::gcd(gb, x);
                    ndp[ga * N + ngb] = (ndp[ga * N + ngb] + c) % MOD;
                }
            }
            dp = std::move(ndp);
        }
        long long ans = 0;
        for (int g = 1; g < N; ++g) ans = (ans + dp[g * N + g]) % MOD;
        return (int)ans;
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
	return solution.subsequencePairCount(nums);
}
