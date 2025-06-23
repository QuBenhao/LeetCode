//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
  bool isVowel(char c) { return strchr("aeiouAEIOU", c) != nullptr; }

public:
  bool halvesAreAlike(string s) {
    int n = s.size();
    auto begin = s.begin();
    auto half = begin + n / 2;
    int count = 0;
    for (auto it = half; it != s.end(); ++it) {
      if (isVowel(*it)) {
        count++;
      }
      if (isVowel(*begin)) {
        count--;
      }
      ++begin;
    }
    return count == 0;
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
  return solution.halvesAreAlike(s);
}
