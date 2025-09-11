//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

constexpr string VOWELS = "aeiou";

class Solution {
public:
  bool doesAliceWin(const string &s) {
    return std::any_of(s.begin(), s.end(), [](const char c) -> bool {
      return VOWELS.find(c) != VOWELS.npos;
    });
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
  return solution.doesAliceWin(s);
}
