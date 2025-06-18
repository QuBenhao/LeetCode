//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> divideArray(vector<int> &nums, int k) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    vector<vector<int>> result(n / 3);
    for (int i = 0, idx = 0; i < n; i += 3, ++idx) {
      if (nums[i + 2] - nums[i] > k) {
        return {};
      }
      result[idx] = {nums[i], nums[i + 1], nums[i + 2]};
    }
    return result;
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
  int k = json::parse(inputArray.at(1));
  return solution.divideArray(nums, k);
}
