//go:build ignore
#include "cpp/common/Solution.h"
#include <ranges>
#include <string_view>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int canBeTypedWords(const string &text, const string &brokenLetters) {
    int ans = 0;
    std::string_view words{text}, delimiters{" "};
    for (const auto &t : std::ranges::split_view(words, delimiters)) {
      if (std::all_of(t.begin(), t.end(), [&brokenLetters](const char &c) -> bool {
            return brokenLetters.find(c) == std::string::npos;
          })) {
        ++ans;
      }
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
  string text = json::parse(inputArray.at(0));
  string brokenLetters = json::parse(inputArray.at(1));
  return solution.canBeTypedWords(text, brokenLetters);
}
