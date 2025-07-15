//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maximumLength(const vector<int> &nums) {
    int ans = 0;
    vector<int> lengths(4, 0);
    for (int num : nums) {
      int cur = num % 2;
      for (int i = 0; i < 4; ++i) {
        if (((i >> (lengths[i] & 1)) & 1) == cur) {
          ans = max(ans, ++lengths[i]);
        }
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
  return solution.maximumLength(nums);
}
