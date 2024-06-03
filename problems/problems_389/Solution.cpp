//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    char findTheDifference(string s, string t) {
        unordered_map<char, int> cs, ct;
        for (int i = 0; i < s.length(); i++) {
            cs[s[i]]++;
            ct[t[i]]++;
        }
        ct[t[t.length() - 1]]++;
        for (auto & it : ct) {
            char key = it.first;
            if (cs.find(key) == cs.end() || it.second > cs[key]) {
                return key;
            }
        }
        return 'e';
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
	return std::string(1, solution.findTheDifference(s, t));
}
