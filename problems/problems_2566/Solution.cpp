//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>
#include <string>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minMaxDifference(int num) {
    string s = to_string(num);
    string t = s;
    int mx = num;
    size_t pos = s.find_first_not_of('9');
    if (pos != string::npos) {
      char a = s[pos];
      replace(s.begin(), s.end(), a, '9');
      mx = stoi(s);
    }
    char b = t[0];
    replace(t.begin(), t.end(), b, '0');
    return mx - stoi(t);
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
  int num = json::parse(inputArray.at(0));
  return solution.minMaxDifference(num);
}
