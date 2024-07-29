//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>
#include <sstream>
#include <iostream>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string decodeString(string s) {
        stack<int> num_stack;
        stack<string> str_stack;
        stringstream ss;
        int times = 0;
        for (auto c: s) {
            if (c == '[') {
                num_stack.push(times);
                times = 0;
                str_stack.push(ss.str());
                ss.str("");
            } else if (c == ']') {
                auto t = num_stack.top();
                auto last_str = str_stack.top();
                num_stack.pop();
                str_stack.pop();
                stringstream tmp;
                tmp << last_str;
                for (int i = 0; i < t; i++) {
                    tmp << ss.str();
                }
                ss.str("");
                ss << tmp.str();
            } else if (c >= '0' && c <= '9') {
                times = times * 10 + c - '0';
            } else {
                ss << c;
            }
        }
        return ss.str();
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
	return solution.decodeString(s);
}
