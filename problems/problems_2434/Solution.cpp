//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>
#include <sstream>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string robotWithString(string s) {
		int n = s.size();
        vector<char> suf(n + 1, 'z');
		for (int i = n - 1; i >= 0; --i) {
			suf[i] = min(suf[i + 1], s[i]);
		}
		stringstream ans;
		stack<char> st;
		for (int i = 0; i < n; ++i) {
			st.push(s[i]);
			while (!st.empty() && st.top() <= suf[i+1]) {
				ans << st.top();
				st.pop();
			}
		}
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
	return solution.robotWithString(s);
}
