//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
private:
    int fastPowMod(int base, int exp, int mod) {
        int result = 1;
        while (exp > 0) {
            if (exp & 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }
public:
    vector<int> getGoodIndices(vector<vector<int>>& variables, int target) {
        int n = static_cast<int>(variables.size());
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            auto a = variables[i][0], b = variables[i][1], c = variables[i][2], m = variables[i][3];
            if (fastPowMod(fastPowMod(a, b, 10), c, m) == target) {
                ans.emplace_back(i);
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
	vector<vector<int>> variables = json::parse(inputArray.at(0));
	int target = json::parse(inputArray.at(1));
	return solution.getGoodIndices(variables, target);
}
