//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool canReachCorner(int xCorner, int yCorner, vector<vector<int>>& circles) {
        
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
	int xCorner = json::parse(inputArray.at(0));
	int yCorner = json::parse(inputArray.at(1));
	vector<vector<int>> circles = json::parse(inputArray.at(2));
	return solution.canReachCorner(xCorner, yCorner, circles);
}
