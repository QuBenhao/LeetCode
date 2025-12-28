//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        
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
	int cost1 = json::parse(inputArray.at(0));
	int cost2 = json::parse(inputArray.at(1));
	int costBoth = json::parse(inputArray.at(2));
	int need1 = json::parse(inputArray.at(3));
	int need2 = json::parse(inputArray.at(4));
	return solution.minimumCost(cost1, cost2, costBoth, need1, need2);
}
