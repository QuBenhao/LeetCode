//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long countCompleteDayPairs(vector<int> &hours) {
    int64_t ans = 0;
    vector<int64_t> hs(24, 0);
    for (int h : hours) {
      hs[h % 24]++;
    }
    for (int i = 1; i < 12; i++) {
      ans += hs[i] * hs[24 - i];
    }
    ans += hs[0] * (hs[0] - 1) / 2;
    ans += hs[12] * (hs[12] - 1) / 2;
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
	vector<int> hours = json::parse(inputArray.at(0));
	return solution.countCompleteDayPairs(hours);
}
