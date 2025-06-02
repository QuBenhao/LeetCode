//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.length();
        int index[26];
        for (int i = 0; i < n; i++) {
            int idx = s[i] - 'a';
            index[idx] = i;
        }
        vector<int> ans;
        for (int i = 0, start = 0, end = 0; i < n; i++) {
            end = max(end, index[s[i] - 'a']);
            if (i == end) {
                ans.push_back(end-start+1);
                start = end+1;
            }
        }
        return ans;
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
	return solution.partitionLabels(s);
}
