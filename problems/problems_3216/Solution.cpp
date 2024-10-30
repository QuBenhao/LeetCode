//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string getSmallestString(string s) {
    int n = static_cast<int>(s.size());
    for (int i = 0; i < n - 1; i++) {
      if (s[i] > s[i + 1] && s[i] % 2 == s[i + 1] % 2) {
        return s.substr(0, i) + s[i + 1] + s[i] + s.substr(i + 2);
      }
    }
    return s;
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
  return solution.getSmallestString(s);
}
