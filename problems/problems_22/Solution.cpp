//go:build ignore
#include "cpp/common/Solution.h"
#include <string>
#include <sstream>
#include <vector>
#include <functional>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
		vector<string> ans;
		function<void(stringstream&, int, int)> backtrack = [&](stringstream &s, int left, int right) {
			if (left == n && right == n) {
				ans.emplace_back(s.str());
				return ;
			}
			if (left < n) {
				s << '(';
				backtrack(s, left + 1, right);
				s.seekp(s.tellp() - static_cast<streampos>(1));
			}
			if (right < left) {
				s << ')';
				backtrack(s, left, right + 1);
				s.seekp(s.tellp() - static_cast<streampos>(1));
			}
		};
		stringstream s;
		backtrack(s, 0, 0);
		return ans;
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
	int n = json::parse(inputArray.at(0));
	return solution.generateParenthesis(n);
}
