//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long bowlSubarrays(const vector<int> &nums) {
    int n = nums.size();
    vector<int> left_greater(n, -1), right_greater(n, -1);
    stack<int> st;
    for (int i = 0; i < n; ++i) {
      while (!st.empty() && nums[st.top()] < nums[i]) {
        right_greater[st.top()] = i;
        st.pop();
      }
      if (!st.empty()) {
        left_greater[i] = st.top();
      }
      st.push(i);
    }
    set<pair<int, int>> s;
    for (int i = 0; i < n; ++i) {
      if (left_greater[i] != -1 && right_greater[i] != -1) {
        s.emplace(left_greater[i], right_greater[i]);
      }
    }
    return s.size();
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
  return solution.bowlSubarrays(nums);
}
