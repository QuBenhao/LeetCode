//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool validateStackSequences(const vector<int> &pushed,
                              const vector<int> &popped) {
    stack<int> st;
    int j = 0, n = popped.size();
    for (const auto &x : pushed) {
      st.push(x);
      while (!st.empty() && j < n && st.top() == popped[j]) {
        st.pop();
        j++;
      }
    }
    return st.empty();
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
  vector<int> pushed = json::parse(inputArray.at(0));
  vector<int> popped = json::parse(inputArray.at(1));
  return solution.validateStackSequences(pushed, popped);
}
