//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        
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
	vector<vector<int>> routes = json::parse(inputArray.at(0));
	int source = json::parse(inputArray.at(1));
	int target = json::parse(inputArray.at(2));
	return solution.numBusesToDestination(routes, source, target);
}
