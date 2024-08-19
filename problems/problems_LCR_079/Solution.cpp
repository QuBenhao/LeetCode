//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> subsets(vector<int> &nums) {
    vector<vector<int>> res;
    function<void(size_t, vector<int> &)> dfs = [&](size_t idx,
                                                    vector<int> &path) {
      if (idx == nums.size()) {
        res.push_back(path);
        return;
      }
      dfs(idx + 1, path);
      path.push_back(nums[idx]);
      dfs(idx + 1, path);
      path.pop_back();
    };
    vector<int> path;
    dfs(0, path);
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
  vector<int> nums = json::parse(inputArray.at(0));
  return solution.subsets(nums);
}
