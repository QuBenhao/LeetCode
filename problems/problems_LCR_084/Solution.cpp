//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> permuteUnique(vector<int> &nums) {
    dfs(nums, 0);
    return res;
  }

private:
  vector<vector<int>> res;
  void dfs(vector<int> nums, int x) {
    if (x == nums.size() - 1) {
      res.push_back(nums);  // 添加排列方案
      return;
    }
    set<int> st;
    for (int i = x; i < nums.size(); i++) {
      if (st.find(nums[i]) != st.end())
        continue;  // 重复，因此剪枝
      st.insert(nums[i]);
      swap(nums[i], nums[x]);  // 交换，将 nums[i] 固定在第 x 位
      dfs(nums, x + 1);       // 开启固定第 x + 1 位元素
      swap(nums[i], nums[x]);  // 恢复交换
    }
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
  return solution.permuteUnique(nums);
}
