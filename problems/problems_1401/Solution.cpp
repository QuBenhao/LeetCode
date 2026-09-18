//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        
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
	int radius = json::parse(inputArray.at(0));
	int xCenter = json::parse(inputArray.at(1));
	int yCenter = json::parse(inputArray.at(2));
	int x1 = json::parse(inputArray.at(3));
	int y1 = json::parse(inputArray.at(4));
	int x2 = json::parse(inputArray.at(5));
	int y2 = json::parse(inputArray.at(6));
	return solution.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2);
}
