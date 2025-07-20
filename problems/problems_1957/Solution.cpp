//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string makeFancyString(const string &s) {
    string result;
    int count = 0;
    for (const auto &c : s) {
      if (result.empty() || result.back() != c) {
        result += c;
        count = 1;
      } else {
        if (count < 2) {
          result += c;
          count++;
        }
      }
    }
    return result;
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
  return solution.makeFancyString(s);
}
