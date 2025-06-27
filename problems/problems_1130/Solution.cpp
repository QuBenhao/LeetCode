//go:build ignore
#include "cpp/common/Solution.h"

#include <stack>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int mctFromLeafValues(const vector<int> &arr) {
    stack<int> st;
    int ans = 0;
    for (auto x : arr) {
      while (!st.empty() && st.top() <= x) {
        int mid = st.top();
        st.pop();
        if (st.empty() || st.top() > x) {
          ans += mid * x;
        } else {
          ans += mid * st.top();
        }
      }
      st.push(x);
    }
    while (st.size() > 1) {
      int mid = st.top();
      st.pop();
      ans += mid * st.top();
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
  vector<int> arr = json::parse(inputArray.at(0));
  return solution.mctFromLeafValues(arr);
}
