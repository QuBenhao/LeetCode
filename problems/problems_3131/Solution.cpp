//go:build ignore
#include "cpp/common/Solution.h"

using std::min;
using json = nlohmann::json;

class Solution {
public:
  int addedInteger(vector<int> &nums1, vector<int> &nums2) {
    int m1 = nums1[0], m2 = nums2[0];
    for (auto v : nums1) {
      m1 = min(m1, v);
    }
    for (auto v : nums2) {
      m2 = min(m2, v);
    }
    return m2 - m1;
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
  vector<int> nums1 = json::parse(inputArray.at(0));
  vector<int> nums2 = json::parse(inputArray.at(1));
  return solution.addedInteger(nums1, nums2);
}
