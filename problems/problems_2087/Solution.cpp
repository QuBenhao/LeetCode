//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
        
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
	vector<int> startPos = json::parse(inputArray.at(0));
	vector<int> homePos = json::parse(inputArray.at(1));
	vector<int> rowCosts = json::parse(inputArray.at(2));
	vector<int> colCosts = json::parse(inputArray.at(3));
	return solution.minCost(startPos, homePos, rowCosts, colCosts);
}
