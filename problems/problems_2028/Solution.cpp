//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	int pos = input.find("\n");
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find("\n");
	}
	inputArray.push_back(input);

	Solution solution;
	vector<int> rolls = json::parse(inputArray.at(0));
	int mean = json::parse(inputArray.at(1));
	int n = json::parse(inputArray.at(2));
	return solution.missingRolls(rolls, mean, n);
}
