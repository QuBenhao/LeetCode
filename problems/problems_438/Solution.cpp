//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
        vector<int> counts(26, 0);
        for (auto c: p) {
            counts[c - 'a']--;
        }
        int diff = 0;
        for (auto c: counts) {
            diff += c != 0;
        }
        int m = static_cast<int>(s.size()), n = static_cast<int>(p.size());
        auto helper = [&counts](int key, int val)-> int {
            bool before = counts[key] == 0;
            counts[key] += val;
            if (before) {
                return 1;
            }
            if (counts[key] == 0) {
                return -1;
            }
            return 0;
        };
        for (int i = 0; i < m; i++) {
            diff += helper(s[i] - 'a', 1);
            if (i >= n - 1) {
                if (diff == 0) {
                    ans.push_back(i - n + 1);
                }
                diff += helper(s[i - n + 1] - 'a', -1);
            }
        }
        return ans;
    }
};

json leetcode::qubh::Solve(string input_json_values) {
	vector<string> inputArray;
	size_t pos = input_json_values.find('\n');
	while (pos != string::npos) {
		inputArray.push_back(input_json_values.substr(0, pos));
		input_json_values = input_json_values.substr(pos + 1);
		pos = input_json_values.find('\n');
	}
	inputArray.push_back(input_json_values);

	Solution solution;
	string s = json::parse(inputArray.at(0));
	string p = json::parse(inputArray.at(1));
	return solution.findAnagrams(s, p);
}
