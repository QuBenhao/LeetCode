//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group;
        for (const string& str: strs) {
            string key = str;
            sort(key.begin(), key.end());
            group[key].push_back(str);
        }
        vector<vector<string>> result;
        for (auto& [key, value]: group) {
            result.push_back(value);
        }
        return result;
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
	vector<string> strs = json::parse(inputArray.at(0));
	return solution.groupAnagrams(strs);
}
