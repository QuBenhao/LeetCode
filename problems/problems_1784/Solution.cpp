//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool checkOnesSegment(const string& s) {
    int count = 0;
    bool appear = false;
    for (char c : s) {
      if (c == '1') {
        appear = true;
      } else {
        if (appear) {
          if (++count > 1) {
            return false;
          }
          appear = false;
        }
      }
    }
    return count == 0 || !appear;
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
  return solution.checkOnesSegment(s);
}
