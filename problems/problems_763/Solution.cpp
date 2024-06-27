//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> last(26, 0);
        for (size_t i = 0; i < s.size(); i++) {
            last[s[i] - 'a'] = i;
        }
        vector<int> res;
        size_t start = 0, end = 0;
        for (size_t i = 0; i < s.size(); i++) {
            end = max(end, static_cast<size_t>(last[s[i] - 'a']));
            if (i == end) {
                res.push_back(end - start + 1);
                start = end + 1;
            }
        }
        return res;
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
