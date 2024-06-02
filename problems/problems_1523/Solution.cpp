//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int countOdds(int low, int high) {
        return (high - low) / 2 + ((low & 1) == 1 || (high & 1) == 1);
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
	int low = json::parse(inputArray.at(0));
	int high = json::parse(inputArray.at(1));
	return solution.countOdds(low, high);
}
