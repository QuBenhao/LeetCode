//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string removeTrailingZeros(string num) {
        size_t idx = num.length() - 1;
        for (; idx >= 0 && num[idx] == '0'; idx--) {
        }
        return num.substr(0, idx + 1);
    }
};

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	string num = json::parse(inputArray.at(0));
	return solution.removeTrailingZeros(num);
}
