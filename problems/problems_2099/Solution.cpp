//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> maxSubsequence(const vector<int> &nums, int k) {
    vector<int> idxes(nums.size());
    iota(idxes.begin(), idxes.end(), 0);
    sort(idxes.begin(), idxes.end(),
         [&nums](int a, int b) { return nums[a] > nums[b]; });
    idxes.resize(k);
    sort(idxes.begin(), idxes.end());
    for (int &idx : idxes) {
      idx = nums[idx];
    }
    return idxes;
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
  return solution.maxSubsequence(nums, k);
}
