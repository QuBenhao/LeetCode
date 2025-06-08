//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
    int dfs(long n, long l, long r) {
        return l <= n ? min(r, n) - l + 1 + dfs(n, l * 10, r * 10 + 9) : 0;
    }
public:
    int findKthNumber(int n, int k) {
        int cur = 1;
        while (k > 1) {
            int count = dfs(n, cur, cur);
            if (count < k) {
                k -= count;
                ++cur;
            } else {
                cur *= 10;
                --k;
            }
        }
        return cur;
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
	int k = json::parse(inputArray.at(1));
	return solution.findKthNumber(n, k);
}
