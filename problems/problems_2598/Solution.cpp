//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int findSmallestInteger(const vector<int> &nums, int value) {
    vector<int> counts(value);
    for (const auto &num : nums) {
      ++counts[(num % value + value) % value];
    }
    int m = *min_element(counts.begin(), counts.end());
    return m * value + (find(counts.begin(), counts.end(), m) - counts.begin());
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
  int value = json::parse(inputArray.at(1));
  return solution.findSmallestInteger(nums, value);
}
