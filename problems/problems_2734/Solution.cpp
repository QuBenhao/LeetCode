//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    string smallestString(string s) {
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s[i] > 'a') {
                for (; i < n && s[i] > 'a'; i++) {
                    s[i]--;
                }
                return s;
            }
        }
        s.back() = 'z';
        return s;
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
	string s = json::parse(inputArray.at(0));
	return solution.smallestString(s);
}
