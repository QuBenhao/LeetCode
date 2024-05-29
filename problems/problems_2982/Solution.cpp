//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumLength(string s) {
        
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
	string s = json::parse(inputArray.at(0));
	return solution.maximumLength(s);
}
