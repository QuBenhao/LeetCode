//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  char processStr(const string &s, long long k) {
    uint64_t length = 0;
    int n = s.length();
    unordered_set<int> invalids;
    for (int i = 0; i < n; ++i) {
      char c = s[i];
      if (c == '#') {
        length *= 2;
      } else if (c == '*') {
        if (length > 0) {
          --length;
        } else {
          invalids.insert(i);
        }
      } else if (c != '%') {
        length += 1;
      }
    }
    if (k >= length) {
      return '.';
    }
    for (int i = n - 1; i >= 0; --i) {
      char c = s[i];
      if (c == '#') {
        length /= 2;
        k %= length;
      } else if (c == '*') {
        ++length;
      } else if (c == '%') {
        k = length - 1 - k;
      } else {
        if (k == length - 1) {
          return c;
        }
        --length;
      }
    }
    return s[k];
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
  long long k = json::parse(inputArray.at(1));
  return std::string(1, solution.processStr(s, k));
}
