//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numRookCaptures(vector<vector<char>>& board) {
        
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
	vector<vector<string>> board_str = json::parse(inputArray.at(0));
	auto board = vector<vector<char>>(board_str.size(), vector<char>(board_str[0].size()));
	for (int i = 0; i < board.size(); i++) {
		for (int j = 0; j < board[i].size(); j++) {
			board[i][j] = board_str[i][j][0];
		}
	}
	return solution.numRookCaptures(board);
}
