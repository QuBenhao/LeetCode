//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {

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
	string beginWord = json::parse(inputArray.at(0));
	string endWord = json::parse(inputArray.at(1));
	vector<string> wordList = json::parse(inputArray.at(2));
	return solution.ladderLength(beginWord, endWord, wordList);
}
