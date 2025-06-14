//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxDiff(int num) {
    string s = to_string(num);

    auto replace_stoi = [&](char old_char, char new_char) {
      int x = 0;
      for (auto c : s) {
        if (c == old_char) {
          x = x * 10 + new_char - '0';
        } else {
          x = x * 10 + c - '0';
        }
      }
      return x;
    };
    int n = s.length();
    int mx, mn;
    int idx = 0;
    while (idx < n && s[idx] == '9') {
      ++idx;
    }
    if (idx == n) {
      mx = num;
    } else {
      mx = replace_stoi(s[idx], '9');
    }
    if (s[0] == '1') {
      idx = 1;
      while (idx < n && (s[idx] == '0' || s[idx] == '1')) {
        ++idx;
      }
      if (idx == n) {
        mn = num;
      } else {
        mn = replace_stoi(s[idx], '0');
      }
    } else {
      mn = replace_stoi(s[0], '1');
    }
    return mx - mn;
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
  return solution.maxDiff(num);
}
