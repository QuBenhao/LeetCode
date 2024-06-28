//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int paintWalls(vector<int>& cost, vector<int>& time) {
        auto n = cost.size();
        auto f = vector<int>(n + 1, INT32_MAX / 2);
        f[0] = 0;
        for (size_t i = 0; i < n; i++) {
            auto t = time[i] + 1;
            for (size_t j = n; j > 0; j--) {
                f[j] =
                    min(f[j], f[j >= t ? j - t : 0] + cost[i]);
            }
        }
        return f[n];
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
	vector<int> cost = json::parse(inputArray.at(0));
	vector<int> time = json::parse(inputArray.at(1));
	return solution.paintWalls(cost, time);
}
