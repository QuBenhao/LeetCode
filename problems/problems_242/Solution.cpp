//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        auto counter = vector<int>(26);
        for (int i = 0; i < s.length(); i++) {
            counter[s[i] - 'a']++;
            counter[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (counter[i] != 0) {
                return false;
            }
        }
        return true;
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
	string s = json::parse(inputArray.at(0));
	string t = json::parse(inputArray.at(1));
	return solution.isAnagram(s, t);
}
