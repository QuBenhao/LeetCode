//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int temperatureTrend(vector<int>& temperatureA, vector<int>& temperatureB) {
        int ans = 0;
        for (int i = 1, cur = 0; i < static_cast<int>(temperatureA.size()); i++) {
            int d1 = temperatureA[i] - temperatureA[i - 1], d2 = temperatureB[i] - temperatureB[i - 1];
            if ((d1 * d2 > 0) || (d1 == 0 && d2 == 0)) {
                cur++;
                ans = max(ans, cur);
            } else {
                cur = 0;
            }
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<int> temperatureA = json::parse(inputArray.at(0));
	vector<int> temperatureB = json::parse(inputArray.at(1));
	return solution.temperatureTrend(temperatureA, temperatureB);
}
