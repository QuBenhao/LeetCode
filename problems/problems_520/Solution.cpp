//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool detectCapitalUse(string word) {
        if (isupper(word[word.length() - 1])) {
            for (size_t i = 0; i < word.length(); i++) {
                if (islower(word[i])) {
                    return false;
                }
            }
        } else if(isupper(word[0])) {
            for (size_t i = 1; i < word.length(); i++) {
                if (isupper(word[i])) {
                    return false;
                }
            }
        } else {
            for (size_t i = 0; i < word.length(); i++) {
                if (isupper(word[i])) {
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
	string word = json::parse(inputArray.at(0));
	return solution.detectCapitalUse(word);
}
