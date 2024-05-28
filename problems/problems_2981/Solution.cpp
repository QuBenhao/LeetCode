//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int maximumLength(string s) {
        vector<int> groups[26];
        for (int i = 0, count = 0, n = s.length(); i < n; i++) {
            count++;
            if (i == n - 1 || s[i] != s[i + 1]) {
                groups[s[i] - 'a'].push_back(count);
                count = 0;
            }
        }
        int ans = 0;
        for (auto& a: groups) {
            if (a.empty()) {
                continue;
            }
            ranges::sort(a, greater());
            a.push_back(0);
            a.push_back(0);
            ans = max({ans, a[0] - 2, min(a[0] - 1, a[1]), a[2]});
        }
        return ans ? ans : -1;
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
	return solution.maximumLength(s);
}
