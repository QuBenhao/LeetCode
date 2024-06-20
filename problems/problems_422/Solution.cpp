//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool validWordSquare(vector<string>& words) {
        for (size_t i = 0; i < words.size(); i++) {
            if (words[i].length() > words.size()) {
                return false;
            }
            for (size_t j = 0; j < i; j++) {
                if ((words[i].length() <= j) != (words[j].length() <= i)) {
                    return false;
                } else if (words[i].length() > j && words[i][j] != words[j][i]) {
                    return false;
                }
            }
        }
        return true;
    }
};

json leetcode::qubh::Solve(string input) {
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	vector<string> words = json::parse(inputArray.at(0));
	return solution.validWordSquare(words);
}
