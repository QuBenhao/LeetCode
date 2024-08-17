//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool checkInclusion(string s1, string s2) {
    vector<int> cnt1(26, 0), cnt2(26, 0);
    int m = static_cast<int>(s1.length()), n = static_cast<int>(s2.length());
    for (auto c : s1) {
      cnt1[c - 'a']++;
    }
    for (int i = 0; i < n; i++) {
      cnt2[s2[i] - 'a']++;
      if (i >= m - 1) {
        if (cnt1 == cnt2) {
          return true;
        }
        cnt2[s2[i - m + 1] - 'a']--;
      }
    }
    return false;
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
  string s1 = json::parse(inputArray.at(0));
  string s2 = json::parse(inputArray.at(1));
  return solution.checkInclusion(s1, s2);
}
