//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int generateKey(int num1, int num2, int num3) {
        
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
	int num1 = json::parse(inputArray.at(0));
	int num2 = json::parse(inputArray.at(1));
	int num3 = json::parse(inputArray.at(2));
	return solution.generateKey(num1, num2, num3);
}
