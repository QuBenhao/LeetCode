//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long maxEnergyBoost(vector<int>& a, vector<int>& b) {
        int n = a.size();
        vector<array<long long, 2>> f(n + 2);
        for (int i = 0; i < n; i++) {
            f[i + 2][0] = max(f[i + 1][0], f[i][1]) + a[i];
            f[i + 2][1] = max(f[i + 1][1], f[i][0]) + b[i];
        }
        return max(f[n + 1][0], f[n + 1][1]);
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
	vector<int> energyDrinkA = json::parse(inputArray.at(0));
	vector<int> energyDrinkB = json::parse(inputArray.at(1));
	return solution.maxEnergyBoost(energyDrinkA, energyDrinkB);
}
