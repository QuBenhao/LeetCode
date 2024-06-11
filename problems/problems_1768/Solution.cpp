//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ans;
        int m = min(word1.length(), word2.length());
        for (int i = 0; i < m; i++) {
            ans += word1[i];
            ans += word2[i];
        }
        ans += word1.substr(m, word1.length());
        ans += word2.substr(m, word2.length());
        return ans;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	size_t pos = input.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find('\n');
	}
	inputArray.push_back(input);

	Solution solution;
	string word1 = json::parse(inputArray.at(0));
	string word2 = json::parse(inputArray.at(1));
	return solution.mergeAlternately(word1, word2);
}
