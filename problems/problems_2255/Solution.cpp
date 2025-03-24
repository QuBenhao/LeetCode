//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int countPrefixes(vector<string>& words, string s) {
		int ans = 0;
		for (const auto &word: words) {
			if (!s.compare(0, word.size(), word)) {
				ans++;
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
	vector<string> words = json::parse(inputArray.at(0));
	string s = json::parse(inputArray.at(1));
	return solution.countPrefixes(words, s);
}
