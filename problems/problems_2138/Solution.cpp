//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<string> divideString(string s, int k, char fill) {
    vector<string> ans;
    int n = s.length();
    for (int i = 0; i < n; i += k) {
      if (i + k <= n) {
        ans.push_back(s.substr(i, k));
      } else {
        ans.push_back(s.substr(i) + string(i + k - n, fill));
      }
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
  string s = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  string fill_string = json::parse(inputArray.at(2));
  char fill = fill_string.length() > 1 ? fill_string[1] : fill_string[0];
  return solution.divideString(s, k, fill);
}
