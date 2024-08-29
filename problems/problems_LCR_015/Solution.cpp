//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> findAnagrams(string s, string p) {
    vector<int> ans;
    vector<int> cnt(26, 0);
    int diff = 0;
    for (char c : p) {
      if (cnt[c - 'a']++ == 0) {
        diff++;
      }
    }
    int m = static_cast<int>(p.size()), n = static_cast<int>(s.size());
    for (int i = 0; i < n; i++) {
      cnt[s[i] - 'a']--;
      if (cnt[s[i] - 'a'] == 0) {
        diff--;
      } else if (cnt[s[i] - 'a'] == -1) {
        diff++;
      }
      if (i >= m - 1) {
        if (diff == 0) {
          ans.push_back(i - m + 1);
        }
        cnt[s[i - m + 1] - 'a']++;
        if (cnt[s[i - m + 1] - 'a'] == 0) {
          diff--;
        } else if (cnt[s[i - m + 1] - 'a'] == 1) {
          diff++;
        }
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
  string s = json::parse(inputArray.at(0));
  string p = json::parse(inputArray.at(1));
  return solution.findAnagrams(s, p);
}
