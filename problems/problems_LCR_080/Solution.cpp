//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> ans;

    function<void(int, vector<int> &)> backtrack = [&](int cur,
                                                       vector<int> &path) {
      if (static_cast<int>(path.size()) == k) {
        ans.push_back(path);
        return;
      }
      for (int i = cur; i <= n; i++) {
        path.push_back(i);
        backtrack(i + 1, path);
        path.pop_back();
      }
    };
    vector<int> path;
    backtrack(1, path);
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
  int k = json::parse(inputArray.at(1));
  return solution.combine(n, k);
}
