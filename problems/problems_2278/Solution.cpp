//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int percentageLetter(string s, char letter) {
        int count = 0;
        for (char c : s) {
            if (c == letter) {
                count++;
            }
        }
        return (count * 100) / s.length();
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
	string letter_string = json::parse(inputArray.at(1));
	char letter = letter_string.length() > 1 ? letter_string[1] : letter_string[0];
	return solution.percentageLetter(s, letter);
}
