//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> permute(vector<int> &nums) {
    vector<vector<int>> res;
    vector<int> path;
    function<void(int)> backtracking = [&](int index) {
      if (index == nums.size()) {
        res.push_back(path);
        return;
      }
      for (int i = 0; i < nums.size(); i++) {
        if (find(path.begin(), path.end(), nums[i]) != path.end()) {
          continue;
        }
        path.push_back(nums[i]);
        backtracking(index + 1);
        path.pop_back();
      }
    };
    backtracking(0);
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
  return solution.permute(nums);
}
