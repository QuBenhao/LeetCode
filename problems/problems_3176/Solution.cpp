//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maximumLength(vector<int> &nums, int k) {
    unordered_map<int, vector<int>> fs;
    vector<int> mx(k + 2);
    for (int x : nums) {
      auto &f = fs[x];
      f.resize(k + 1);
      for (int j = k; j >= 0; j--) {
        f[j] = max(f[j], mx[j]) + 1;
        mx[j + 1] = max(mx[j + 1], f[j]);
      }
    }
    return mx[k + 1];
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
  return solution.maximumLength(nums, k);
}
