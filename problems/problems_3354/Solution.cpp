//go:build ignore
#include "cpp/common/Solution.h"
#include <numeric>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int countValidSelections(const vector<int> &nums) {
    int sum = reduce(nums.begin(), nums.end());
    int ans = 0, pre = 0;
    for (const auto &num : nums) {
      if (num != 0) {
        pre += num;
      } else {
        int d = pre << 1;
        if (d == sum) {
          ans += 2;
        } else if (abs(d - sum) == 1) {
          ans += 1;
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
  return solution.countValidSelections(nums);
}
