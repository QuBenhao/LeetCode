//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minimumCost(int m, int n, vector<int>& horizontalCut, vector<int>& verticalCut) {
        
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
	int m = json::parse(inputArray.at(0));
	int n = json::parse(inputArray.at(1));
	vector<int> horizontalCut = json::parse(inputArray.at(2));
	vector<int> verticalCut = json::parse(inputArray.at(3));
	return solution.minimumCost(m, n, horizontalCut, verticalCut);
}
