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
      res.push_back(nums);  // Add the permutation
      return;
    }
    set<int> st;
    for (int i = x; i < nums.size(); i++) {
      if (st.find(nums[i]) != st.end())
        continue;  // Prune duplicates
      st.insert(nums[i]);
      swap(nums[i], nums[x]);  // Swap to fix nums[i] at position x
      dfs(nums, x + 1);       // Start fixing the element at position x + 1
      swap(nums[i], nums[x]);  // Undo the swap
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
