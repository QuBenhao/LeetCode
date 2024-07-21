//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }
        auto translator = map<char, string>{
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        vector<string> ans;
        function<void(int, string)> dfs = [&](int index, const string& path) {
            if (index == digits.size()) {
                ans.push_back(path);
                return;
            }
            for (auto c: translator[digits[index]]) {
                dfs(index + 1, path + c);
            }
        };
        dfs(0, "");
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
	string digits = json::parse(inputArray.at(0));
	return solution.letterCombinations(digits);
}
