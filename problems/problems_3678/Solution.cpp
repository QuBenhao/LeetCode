//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int smallestAbsent(const vector<int> &nums) {
    unordered_set<int> s;
    int sm = 0;
    int mx = 0;
    int n = nums.size();
    for (const auto &num : nums) {
      s.insert(num);
      sm += num;
      mx = max(mx, num);
    }
    int avg = ceil(static_cast<double>(sm + 1) / n);
    for (int i = max(1, avg); i <= mx + 1; ++i) {
      if (!s.contains(i)) {
        return i;
      }
    }
    return 1;
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
  return solution.smallestAbsent(nums);
}
