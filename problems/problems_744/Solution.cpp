//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        
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
	vector<string> letters_str = json::parse(inputArray.at(0));
	auto letters = vector<char>(letters_str.size());
	for (size_t i = 0; i < letters.size(); ++i) {
		letters[i] = letters_str[i][0];
	}
	string target_string = json::parse(inputArray.at(1));
	char target = target_string.length() > 1 ? target_string[1] : target_string[0];
	return std::string(1, solution.nextGreatestLetter(letters, target));
}
