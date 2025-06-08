//go:build ignore
#include "cpp/common/Solution.h"

#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minOperations(string word1, string word2) {
        auto update = [](unordered_map<int, int>& cnt, char a, char b, int& op) {
            if (a == b) {
                return;
            }
            int h = (b - 'a') * 26 + (a - 'a');
            if (cnt[h] > 0) {
                cnt[h]--;
            } else {
                cnt[(a-'a') * 26 + (b - 'a')]++;
                ++op;
            }
        };
        int n = word1.length();

        vector<vector<int>> rev_op(n, vector<int>(n, 0));
        for (int i = 0; i < 2 * n - 1; ++i) {
            int l = i / 2, r = (i + 1) / 2;
            int op = 1; // reverse operation
            unordered_map<int, int> cnt;
            while (l >= 0 && r < n) {
                update(cnt, word1[l], word2[r], op);
                if (l != r) {
                    update(cnt, word1[r], word2[l], op);
                }
                rev_op[l][r] = op;
                --l;
                ++r;
            }
        }

        vector<int> dp(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            int op = 0;
            int res = INT_MAX;
            unordered_map<int, int> cnt;
            for (int j = i; j >= 0; --j) {
                update(cnt, word1[j], word2[j], op);
                res = min(res, dp[j] + min(op, rev_op[j][i]));
            }
            dp[i + 1] = res;
        }
        return dp[n];
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
	string word1 = json::parse(inputArray.at(0));
	string word2 = json::parse(inputArray.at(1));
	return solution.minOperations(word1, word2);
}
