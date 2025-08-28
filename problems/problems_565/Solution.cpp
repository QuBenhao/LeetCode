//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int arrayNesting(const vector<int> &nums) {
    int n = nums.size();
    vector<bool> visited(n, false);
    int ans = 0;
    for (int i = 0; i < n; ++i) {
      if (visited[i])
        continue;
      int cur = 1, j = nums[i];
      visited[i] = true;
      while (j != i) {
        visited[j] = true;
        j = nums[j];
        ++cur;
      }
      ans = max(ans, cur);
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
  return solution.arrayNesting(nums);
}
