//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<string> validStrings(int n) {
    vector<string> ans;
    string path(n, 0);
    function<void(int)> dfs = [&](int i) -> void {
      if (i == n) {
        ans.push_back(path);
        return;
      }
      if (i == 0 || path[i - 1] == '1') {
        path[i] = '0';
        dfs(i + 1);
      }
      path[i] = '1';
      dfs(i + 1);
    };
    dfs(0);
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
  int n = json::parse(inputArray.at(0));
  return solution.validStrings(n);
}
