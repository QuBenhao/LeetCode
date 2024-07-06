//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        auto ans = 0;
        for (int i = 0, j = -1; i < static_cast<int>(s.length()); i++) {
            if (map.find(s[i]) != map.end()) {
                j = max(j, map[s[i]]);
            }
            ans = max(ans, i - j);
            map[s[i]] = i;
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input)
{
	vector<string> inputArray;
	int pos = input.find("\n");
	while (pos != string::npos) {
		inputArray.push_back(input.substr(0, pos));
		input = input.substr(pos + 1);
		pos = input.find("\n");
	}
	inputArray.push_back(input);

	Solution solution;
	string s = json::parse(inputArray.at(0));
	return solution.lengthOfLongestSubstring(s);
}
