//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    void reverseString(vector<char>& s) {
        
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
	vector<string> s_str = json::parse(inputArray.at(0));
	auto s = vector<char>(s_str.size());
	for (int i = 0; i < s.size(); i++) {
		s[i] = s_str[i][0];
	}
	solution.reverseString(s);
	return s;
}
