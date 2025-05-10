//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

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
	vector<int> piles = json::parse(inputArray.at(0));
	int h = json::parse(inputArray.at(1));
	return solution.minEatingSpeed(piles, h);
}
