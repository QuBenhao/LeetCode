//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>
#include <vector>
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        unordered_map<char, vector<int>> idx_map(26);
		for (int i = 0; i < s.size(); ++i) {
			idx_map[s[i]].push_back(i);
		}
		int ans = 0;
		for (const auto& word: words) {
			int idx = 0, m = word.size();
			int s_idx = -1;
			while (idx < m) {
				auto it = idx_map.find(word[idx]);
				if (it == idx_map.end()) {
					break;
				}
				auto &arr = it->second;
				auto next_it = upper_bound(arr.begin(), arr.end(), s_idx);
				if (next_it == arr.end()) {
					break;
				}
				s_idx = *next_it;
				++idx;
			}
			ans += (idx == m);
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
	vector<string> words = json::parse(inputArray.at(1));
	return solution.numMatchingSubseq(s, words);
}
