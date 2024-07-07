//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        string left = "([{", right = ")]}";
        for (auto c: s) {
            if (left.find(c) != string::npos) {
                stack.push(c);
            } else if (stack.empty() || stack.top() != left[right.find(c)]) {
                return false;
            } else {
                stack.pop();
            }
        }
        return stack.empty();
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
	string s = json::parse(inputArray.at(0));
	return solution.isValid(s);
}
