//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool areAlmostEqual(const string &s1, const string &s2) {
    int d1 = -1, d2 = -1;
    int n = s1.size();
    for (int i = 0; i < n; ++i) {
      if (s1[i] != s2[i]) {
        if (d1 == -1) {
          d1 = i;
        } else if (d2 == -1) {
          d2 = i;
        } else {
          return false;
        }
      }
    }
    if (d1 == -1)
      return true;
    if (d2 == -1)
      return false;
    return s1[d1] == s2[d2] && s1[d2] == s2[d1];
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
  string s1 = json::parse(inputArray.at(0));
  string s2 = json::parse(inputArray.at(1));
  return solution.areAlmostEqual(s1, s2);
}
