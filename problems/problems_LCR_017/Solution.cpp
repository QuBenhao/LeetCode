//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string minWindow(string s, string t) {
    int ans_left = -1, ans_right = -1;
    int left = 0, right = 0;
    unordered_map<char, int> counter;
    int diff = 0;
    for (const auto &c : t) {
      counter[c]++;
      if (counter[c] == 1) {
        diff++;
      }
    }
    while (right < s.size()) {
      if (counter.find(s[right]) != counter.end()) {
        counter[s[right]]--;
        if (counter[s[right]] == 0) {
          diff--;
        }
      }
      while (diff == 0) {
        if (ans_left == -1 || right - left < ans_right - ans_left) {
          ans_left = left;
          ans_right = right;
        }
        if (counter.find(s[left]) != counter.end()) {
          counter[s[left]]++;
          if (counter[s[left]] == 1) {
            diff++;
          }
        }
        left++;
      }
      right++;
    }
    return ans_left == -1 ? "" : s.substr(ans_left, ans_right - ans_left + 1);
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
  return solution.minWindow(s, t);
}
