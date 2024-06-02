//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_set>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> set(candyType.begin(), candyType.end());
        return min(set.size(), candyType.size() / 2);
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
	vector<int> candyType = json::parse(inputArray.at(0));
	return solution.distributeCandies(candyType);
}
