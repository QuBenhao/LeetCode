//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxXorSubsequences(const vector<int> &nums) {
    array<int, 32> base = {};
    for (auto num : nums) {
      for (int i = 31; i >= 0; --i) {
        if (((num >> i) & 1) == 1) {
          if (base[i] != 0) {
            num ^= base[i];
          } else {
            base[i] = num;
            break;
          }
        }
      }
    }
    int ans = 0;
    for (int i = 31; i >= 0; --i) {
      if (base[i] != 0 && (((ans >> i) & 1) == 0)) {
        ans ^= base[i];
      }
    }
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
  vector<int> nums = json::parse(inputArray.at(0));
  return solution.maxXorSubsequences(nums);
}
