//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        
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
	vector<int> present = json::parse(inputArray.at(1));
	vector<int> future = json::parse(inputArray.at(2));
	vector<vector<int>> hierarchy = json::parse(inputArray.at(3));
	int budget = json::parse(inputArray.at(4));
	return solution.maxProfit(n, present, future, hierarchy, budget);
}
