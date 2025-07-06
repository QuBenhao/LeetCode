//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minMoves(int sx, int sy, int tx, int ty) {
        
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
	int sx = json::parse(inputArray.at(0));
	int sy = json::parse(inputArray.at(1));
	int tx = json::parse(inputArray.at(2));
	int ty = json::parse(inputArray.at(3));
	return solution.minMoves(sx, sy, tx, ty);
}
