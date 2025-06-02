//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        
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
	vector<int> status = json::parse(inputArray.at(0));
	vector<int> candies = json::parse(inputArray.at(1));
	vector<vector<int>> keys = json::parse(inputArray.at(2));
	vector<vector<int>> containedBoxes = json::parse(inputArray.at(3));
	vector<int> initialBoxes = json::parse(inputArray.at(4));
	return solution.maxCandies(status, candies, keys, containedBoxes, initialBoxes);
}
