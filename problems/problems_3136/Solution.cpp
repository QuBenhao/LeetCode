//go:build ignore
#include "cpp/common/Solution.h"
#include <cctype>
#include <string_view>

using namespace std;
using json = nlohmann::json;

constexpr string_view kVowels = "aeiou";
class Solution {
public:
  bool isValid(const string &word) {
    if (word.length() < 3) {
      return false;
    }
    bool has_vowel = false, has_consonant = false;
    for (char c : word) {
      if (isalpha(c)) {
        char lower_c = tolower(c);
        if (kVowels.find(lower_c) != string_view::npos) {
          has_vowel = true;
        } else if (!has_consonant) {
          has_consonant = true;
        }
      } else if (!isdigit(c)) {
        return false;
      }
    }
    return has_vowel && has_consonant;
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
  string word = json::parse(inputArray.at(0));
  return solution.isValid(word);
}
