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
        stack<string> st;
        stack<int> mul;
        stringstream ans;
        stringstream ss;
        int cur = 0;
        for (auto c: s) {
            if (c >= '0' && c <= '9') {
                cur = cur * 10 + (c - '0');
            } else if (c == '[') {
                mul.push(cur);
                cur = 0;
                st.emplace(ss.str());
                ss.str("");
            } else if (c == ']') {
                int m = mul.top();
                mul.pop();
                stringstream tmp;
                for (int i = 0; i < m; i++) {
                    tmp << ss.str();
                }
                ss.str("");
                if (st.empty()) {
                    ans << tmp.str();
                } else {
                    ss << st.top();
                    st.pop();
                    ss << tmp.str();
                }
            } else {
                ss << c;
            }
        }
        ans << ss.str();
        return ans.str();
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
