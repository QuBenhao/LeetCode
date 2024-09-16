//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> combinationSum2(vector<int> &candidates, int target) {
    vector<vector<int>> res;
    vector<int> path;
    sort(candidates.begin(), candidates.end());
    function<void(int, int)> dfs = [&](int idx, int remain) {
      if (remain == 0) {
        res.push_back(path);
        return;
      }
      if (idx == candidates.size() || remain < 0) {
        return;
      }
      for (int i = idx; i < candidates.size(); i++) {
        if (i > idx && candidates[i] == candidates[i - 1]) {
          continue;
        }
        path.push_back(candidates[i]);
        dfs(i + 1, remain - candidates[i]);
        path.pop_back();
      }
    };
    dfs(0, target);
    return res;
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
  vector<int> candidates = json::parse(inputArray.at(0));
  int target = json::parse(inputArray.at(1));
  return solution.combinationSum2(candidates, target);
}
