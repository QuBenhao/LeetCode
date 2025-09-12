//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

constexpr string VOWELS = "aeiou";

class Solution {
public:
  int maxFreqSum(const string &s) {
    array<int, 5> vowels_count = {};
    array<int, 26> non_vowels_count = {};
    for (const auto &c : s) {
      size_t pos = VOWELS.find(c);
      if (pos != std::string::npos) {
        ++vowels_count[pos];
      } else {
        ++non_vowels_count[c - 'a'];
      }
    }
    return *std::max_element(vowels_count.begin(), vowels_count.end()) +
           *std::max_element(non_vowels_count.begin(), non_vowels_count.end());
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
  return solution.maxFreqSum(s);
}
