//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int trap(vector<int> &height) {
    int n = static_cast<int>(height.size());
    vector<int> left_max(n, 0), right_max(n, 0);
    for (int i = 1; i < n; i++) {
      left_max[i] = max(left_max[i - 1], height[i - 1]);
      right_max[n - i - 1] = max(right_max[n - i], height[n - i]);
    }
    int ans = 0;
    for (int i = 0; i < n; i++) {
      int cur = min(left_max[i], right_max[i]);
      ans += max(0, cur - height[i]);
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
  vector<int> height = json::parse(inputArray.at(0));
  return solution.trap(height);
}
