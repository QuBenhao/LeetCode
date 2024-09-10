//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool isAnagram(string s, string t) {
    if (s.size() != t.size() || s == t) {
      return false;
    }
    vector<int> count(26, 0);
    for (size_t i = 0; i < s.size(); ++i) {
      ++count[s[i] - 'a'];
      --count[t[i] - 'a'];
    }
    for (int i = 0; i < 26; ++i) {
      if (count[i] != 0) {
        return false;
      }
    }
    return true;
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
  string t = json::parse(inputArray.at(1));
  return solution.isAnagram(s, t);
}
