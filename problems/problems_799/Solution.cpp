//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    double champagneTower(int poured, int query_row, int query_glass) {
        
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
	int poured = json::parse(inputArray.at(0));
	int query_row = json::parse(inputArray.at(1));
	int query_glass = json::parse(inputArray.at(2));
	return solution.champagneTower(poured, query_row, query_glass);
}
