//go:build ignore
#include "cpp/common/Solution.h"

#include <stack>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string clearStars(string s) {
        stack<int> st[26];
        uint32_t mask = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '*') {
                int k = countr_zero(mask);
                auto& stk = st[k];
                s[stk.top()] = '*';
                stk.pop();
                if (stk.empty()) {
                    mask &= ~(1 << k);
                }
            } else {
                int k = s[i] - 'a';
                st[k].push(i);
                mask |= (1 << k);
            }
        }
        s.erase(ranges::remove(s, '*').begin(), s.end());
        return s;
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
	return solution.clearStars(s);
}
