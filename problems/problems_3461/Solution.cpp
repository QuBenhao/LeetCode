//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool hasSameDigits(const string &s) {
    int n = s.size();
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
      nums[i] = s[i] - '0';
    }
    while ((n = nums.size()) > 2) {
      for (int i = 0; i < n - 1; ++i) {
        nums[i] = (nums[i] + nums[i + 1]) % 10;
      }
      nums.pop_back();
    }
    return nums[0] == nums[1];
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
  string s = json::parse(inputArray.at(0));
  return solution.hasSameDigits(s);
}
