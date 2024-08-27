//go:build ignore
#include "cpp/common/Solution.h"
#include <string>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<string>> partition(string s) {
    int n = static_cast<int>(s.size());
    vector<vector<bool>> dp(n, vector<bool>(n, false));
	for (int i = 0; i < n; i++) {
	  dp[i][i] = true;
	}
    for (int i = n - 1; i >= 0; i--) {
      for (int j = i + 1; j < n; j++) {
        if (s[i] == s[j] && (j - i < 2 || dp[i + 1][j - 1])) {
          dp[i][j] = true;
        }
      }
    }
    vector<vector<string>> ans;
    vector<string> path;
    function<void(int)> backtrack = [&](int i) {
      if (i == n) {
        ans.emplace_back(path);
        return;
      }
      for (int j = i; j < n; j++) {
        if (dp[i][j]) {
          path.emplace_back(s.substr(i, j - i + 1));
          backtrack(j + 1);
          path.pop_back();
        }
      }
    };
	backtrack(0);
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
  return solution.partition(s);
}
