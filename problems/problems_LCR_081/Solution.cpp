//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
    vector<vector<int>> ans;
    int n = static_cast<int>(candidates.size());
    function<void(int, vector<int> &, int)> backtrack =
        [&](int idx, vector<int> &path, int remain) {
          if (remain == 0) {
            ans.push_back(path);
            return;
          }
          if (idx == n) {
            return;
          }
          if (remain - candidates[idx] >= 0) {
            path.push_back(candidates[idx]);
            backtrack(idx, path, remain - candidates[idx]);
            path.pop_back();
          }
          backtrack(idx + 1, path, remain);
        };
    sort(candidates.begin(), candidates.end());
    vector<int> path;
    backtrack(0, path, target);
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
  vector<int> candidates = json::parse(inputArray.at(0));
  int target = json::parse(inputArray.at(1));
  return solution.combinationSum(candidates, target);
}
