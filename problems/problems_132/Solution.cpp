//go:build ignore
#include "cpp/common/Solution.h"


using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int minCut(string s) {
        int n = s.length();
        vector<vector<bool>> is_palindrome(n, vector<bool>(n, false));
        for (int i = 0; i < n; ++i) {
            is_palindrome[i][i] = true;
            for (int j = i - 1; j >= 0; --j) {
                is_palindrome[j][i] = (s[i] == s[j]) && (i - j < 2 || is_palindrome[j + 1][i - 1]);
            }
        }

        vector<int> cuts(n + 1, n);
        cuts[0] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j <= i; ++j) {
                if (is_palindrome[j][i]) {
                    cuts[i + 1] = min(cuts[i + 1], cuts[j] + 1);
                }
            }
        }
        return cuts[n] - 1; // Subtract 1 because cuts[n] counts the number of partitions, not cuts
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
	return solution.minCut(s);
}
