//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  string minWindow(string s, string t) {
    auto getIdx = [](char c) -> int {
      return (c >= 'A' && c <= 'Z') ? c - 'A' : c - 'a' + 26;
    };
    vector<int> cnt_s(52, 0), cnt_t(52, 0);
    int diff = 0;
    for (char c : t) {
      int idx = getIdx(c);
      if (cnt_t[idx]++ == 0) {
        diff++;
      }
    }
    int ans_left = -1, ans_right = -1;
    for (int left = 0, right = 0; right < static_cast<int>(s.size()); right++) {
      int idx = getIdx(s[right]);
      if (++cnt_s[idx] == cnt_t[idx]) {
        diff--;
      }
      while (left < right) {
        int idx = getIdx(s[left]);
        if (cnt_s[idx] > cnt_t[idx] && --cnt_s[idx] >= 0) {
          left++;
        } else {
          break;
        }
      }
      if (diff == 0 &&
          (ans_left == -1 || right - left < ans_right - ans_left)) {
        ans_left = left;
        ans_right = right;
      }
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
