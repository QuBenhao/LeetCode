//go:build ignore
#include "cpp/common/Solution.h"
#include <sstream>
#include <queue>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string clearDigits(string s) {
    deque<char> st;
    for (char c : s) {
      if (c >= '0' && c <= '9') {
        if (!st.empty()) {
          st.pop_back();
        }
      } else {
        st.push_back(c);
      }
    }
    stringstream ss;
    while (!st.empty()) {
      ss << st.front();
      st.pop_front();
    }
    return ss.str();
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
  return solution.clearDigits(s);
}
