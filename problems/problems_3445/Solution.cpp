//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxDifference(string s, int k) {
        int ans = INT_MIN;
		for (int x = 0; x < 5; ++x) {
			for (int y = 0; y < 5; ++y) {
				if (x == y) continue;
				array<int, 5> cur_sum = {0, 0, 0, 0, 0};
				array<int, 5> prev_sum = {0, 0, 0, 0, 0};
				array<array<int, 2>, 2> min_s = {{{INT_MAX >> 2, INT_MAX >> 2}, {INT_MAX >> 2, INT_MAX >> 2}}};
				for (int left = 0, right = 0; right < s.size(); ++right) {
					++cur_sum[s[right] - '0'];
					while (right - left + 1 >= k && cur_sum[x] > prev_sum[x] && cur_sum[y] > prev_sum[y]) {
						int p = prev_sum[x] & 1, q = prev_sum[y] & 1;
						min_s[p][q] = min(min_s[p][q], prev_sum[x] - prev_sum[y]);
						++prev_sum[s[left] - '0'];
						++left;
					}
					if (right + 1 >= k) {
						ans = max(ans, cur_sum[x] - cur_sum[y] - min_s[cur_sum[x] & 1 ^ 1][cur_sum[y] & 1]);
					}
				}
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
	string s = json::parse(inputArray.at(0));
	int k = json::parse(inputArray.at(1));
	return solution.maxDifference(s, k);
}
