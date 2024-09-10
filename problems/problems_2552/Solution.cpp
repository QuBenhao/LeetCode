//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long countQuadruplets(vector<int> &nums) {
    int64_t cnt4 = 0;
    size_t n = nums.size();
    vector<int64_t> cnt3(n);
    for (size_t l = 2; l < n; l++) {
      int64_t cnt2 = 0;
      for (size_t j = 0; j < l; j++) {
        if (nums[j] < nums[l]) {
          cnt4 += cnt3[j];
          cnt2++;
        } else {
          cnt3[j] += cnt2;
        }
      }
    }
    return cnt4;
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
  return solution.countQuadruplets(nums);
}
