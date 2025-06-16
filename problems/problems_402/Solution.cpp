//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string removeKdigits(string num, int k) {
        deque<char> stack;
		for (char c : num) {
			while (k > 0 && !stack.empty() && stack.back() > c) {
				stack.pop_back();
				--k;
			}
			stack.push_back(c);
		}
		while (k > 0 && !stack.empty()) {
			stack.pop_back();
			--k;
		}
		while (!stack.empty() && stack.front() == '0') {
			stack.pop_front();
		}
		if (stack.empty()) {
			return "0";
		}
		return string(stack.begin(), stack.end());
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
	string num = json::parse(inputArray.at(0));
	int k = json::parse(inputArray.at(1));
	return solution.removeKdigits(num, k);
}
