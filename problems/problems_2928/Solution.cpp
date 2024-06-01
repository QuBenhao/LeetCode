//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int distributeCandies(int n, int limit) {
        return combinationTwo(n + 2) - 3 * combinationTwo(n + 1 - limit) + 3 * combinationTwo(n - 2 * limit) -
                combinationTwo(n - 1 - 3 * limit);
    }
private:
    int combinationTwo(int n) {
        return n > 1 ? n * (n - 1) / 2 : 0;
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
	int n = json::parse(inputArray.at(0));
	int limit = json::parse(inputArray.at(1));
	return solution.distributeCandies(n, limit);
}
