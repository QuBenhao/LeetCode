//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string smallestSubsequence(string s, int k, char letter, int repetition) {
    vector<char> stack(k);
    int letter_left = std::count(s.begin(), s.end(), letter);
    int letter_count = 0;
    int idx = 0;
    int n = s.length();
    for (int i = 0; i < n; ++i) {
      char c = s[i];
      while (idx > 0 && stack[idx - 1] > c && n - i + idx - 1 >= k &&
             (c == letter ||
              letter_count + letter_left - (stack[idx - 1] == letter ? 1 : 0) >=
                  repetition)) {
        if (stack[idx - 1] == letter) {
          --letter_count;
        }
        --idx;
      }
      if (idx < k) {
        if (c == letter) {
          ++letter_count;
          stack[idx++] = c;
        } else if (k - idx > repetition - letter_count) {
          stack[idx++] = c;
        }
      }
      if (c == letter) {
        --letter_left;
      }
    }
    return string(stack.begin(), stack.end());
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
  int k = json::parse(inputArray.at(1));
  string letter_string = json::parse(inputArray.at(2));
  char letter =
      letter_string.length() > 1 ? letter_string[1] : letter_string[0];
  int repetition = json::parse(inputArray.at(3));
  return solution.smallestSubsequence(s, k, letter, repetition);
}
