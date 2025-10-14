//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool hasIncreasingSubarrays(const vector<int> &nums, int k) {
    int a = 0, b = k;
    int n = nums.size() - k;
  out:
    while (b <= n) {
      for (int j = a + 1; j < b; ++j) {
        if (nums[j] <= nums[j - 1]) {
          b += j - a;
          a += j - a;
          goto out;
        }
      }
      for (int j = b + 1; j < b + k; ++j) {
        if (nums[j] <= nums[j - 1]) {
          a += j - b;
          b += j - b;
          goto out;
        }
      }
      return true;
    }
    return false;
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
  return solution.hasIncreasingSubarrays(nums, k);
}
