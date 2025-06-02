//go:build ignore
#include "cpp/common/Solution.h"
#include <stack>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<int> st;
        int ans = 0;
        int n = heights.size();
        for (int i = 0; i <= n; i++) {
            while (!st.empty() && (i == n || heights[st.top()] > heights[i])) {
                int idx = st.top();
                st.pop();
                int left = st.empty() ? -1 : st.top();
                ans = max(ans, (i - left -1) * heights[idx]);
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
