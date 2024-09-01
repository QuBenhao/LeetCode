//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int largestRectangleArea(vector<int> &heights) {
    stack<int> st;
    int n = static_cast<int>(heights.size());
    st.push(-1);
    heights.push_back(0);
    int ans = 0;
    for (int i = 0; i <= n; i++) {
      while (st.top() != -1 && heights[st.top()] > heights[i]) {
        int h = heights[st.top()];
        st.pop();
        int w = i - st.top() - 1;
        ans = max(ans, h * w);
      }
      st.push(i);
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
  vector<int> heights = json::parse(inputArray.at(0));
  return solution.largestRectangleArea(heights);
}
