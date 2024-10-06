//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {

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
	int target = json::parse(inputArray.at(0));
	int startFuel = json::parse(inputArray.at(1));
	vector<vector<int>> stations = json::parse(inputArray.at(2));
	return solution.minRefuelStops(target, startFuel, stations);
}
