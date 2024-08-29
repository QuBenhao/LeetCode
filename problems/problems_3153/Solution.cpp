//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long sumDigitDifferences(vector<int> &nums) {
    int length = 0;
    int num = nums[0];
    while (num > 0) {
      num /= 10;
      length++;
    }
    vector<vector<int64_t>> counter =
        vector<vector<int64_t>>(length, vector<int64_t>(10, 0));
    int64_t ans = 0;
    for (size_t i = 0; i < nums.size(); i++) {
      num = nums[i];
      for (int j = 0; j < length; j++) {
        ans += static_cast<int64_t>(i) - counter[j][num % 10];
        counter[j][num % 10]++;
        num /= 10;
      }
    }
    return static_cast<long long>(ans);
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
  return solution.sumDigitDifferences(nums);
}
