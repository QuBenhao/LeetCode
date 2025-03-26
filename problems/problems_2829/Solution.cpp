//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumSum(int n, int k) {
		int ans = 0, cur = 1;
		bool[] explored = new bool[51];
		for (int i = 0; i < n; i++) {
			while (cur < k && explored[k - cur]) {
				cur++;
			}
			ans += cur;
			explored[cur] = true;
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
	int k = json::parse(inputArray.at(1));
	return solution.minimumSum(n, k);
}
