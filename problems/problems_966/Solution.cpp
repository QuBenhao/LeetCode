//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

constexpr string VOWELS = "aeiou";

class Solution {
public:
  vector<string> spellchecker(const vector<string> &wordlist,
                              const vector<string> &queries) {
    unordered_set<string> origin;
    unordered_map<string, string> ignore_cases, ignore_vowels;

    auto strIgnoreVowels = [](string &w) -> void {
      for (auto &c : w) {
        if (VOWELS.find(c) != string::npos) {
          c = '*';
        }
      }
    };

    for (const auto &word : wordlist) {
      origin.insert(word);
      string lower = word;
      std::transform(word.begin(), word.end(), lower.begin(), ::tolower);
      if (ignore_cases.find(lower) == ignore_cases.end()) {
        ignore_cases[lower] = word;
      }
      strIgnoreVowels(lower);
      if (ignore_vowels.find(lower) == ignore_vowels.end()) {
        ignore_vowels[lower] = word;
      }
    }

    vector<string> ans;
    for (const auto &query : queries) {
      if (origin.contains(query)) {
        ans.emplace_back(query);
        continue;
      }
      string lower = query;
      std::transform(query.begin(), query.end(), lower.begin(), ::tolower);
      auto it = ignore_cases.find(lower);
      if (it != ignore_cases.end()) {
        ans.emplace_back(it->second);
        continue;
      }
      strIgnoreVowels(lower);
      it = ignore_vowels.find(lower);
      if (it != ignore_vowels.end()) {
        ans.emplace_back(it->second);
        continue;
      }
      ans.emplace_back("");
    }
    return ans;
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
  vector<string> wordlist = json::parse(inputArray.at(0));
  vector<string> queries = json::parse(inputArray.at(1));
  return solution.spellchecker(wordlist, queries);
}
