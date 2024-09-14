//go:build ignore
#include "cpp/common/Solution.h"
#include <string>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string removeStars(string s) {
			string result;
			for (size_t i = 0, n = s.size(); i < n; i++) {
				if (s[i] == '*') {
					if (!result.empty()) {
						result.pop_back();
					}
				} else {
					result.push_back(s[i]);
				}
			}
			return result;
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
	return solution.removeStars(s);
}
