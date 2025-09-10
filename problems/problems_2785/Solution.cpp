//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>
#include <iterator>

using namespace std;
using json = nlohmann::json;

constexpr std::string VOWELS = "AEIOUaeiou";

class Solution {
public:
  string sortVowels(string &s) {
    auto isVowel = [](char c) -> bool {
      return std::find(VOWELS.begin(), VOWELS.end(), c) != VOWELS.end();
    };

    vector<char> vowels;
    for (char c : s) {
      if (isVowel(c)) {
        vowels.push_back(c);
      }
    }
    sort(vowels.begin(), vowels.end());
    auto it2 = vowels.rbegin();
    for (auto it1 = s.rbegin(); it1 != s.rend() && it2 != vowels.rend();
         it1 = next(it1)) {
      if (isVowel(*it1)) {
        *it1 = *it2;
        it2 = next(it2);
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
  return solution.sortVowels(s);
}
