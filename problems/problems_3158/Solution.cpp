//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_set>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int duplicateNumbersXOR(vector<int> &nums) {
    int ans = 0;
    unordered_set<int> s;
    for (int num : nums) {
      if (s.find(num) != s.end()) {
        ans ^= num;
      } else {
        s.insert(num);
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
  return solution.duplicateNumbersXOR(nums);
}
