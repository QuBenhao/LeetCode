//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int closestTarget(vector<string>& words, string target, int startIndex) {
        
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
	vector<string> words = json::parse(inputArray.at(0));
	string target = json::parse(inputArray.at(1));
	int startIndex = json::parse(inputArray.at(2));
	return solution.closestTarget(words, target, startIndex);
}
