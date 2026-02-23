//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_set>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool hasAllCodes(string s, int k) {
    int n = s.size();
    int target = 1 << k;
    if (n < target + k - 1) {
      return false;
    }
    int cur = 0;
    for (int i = 0; i < k; ++i) {
      cur = cur << 1 | s[i] - '0';
    }
    unordered_set<int> st = {cur};
    int full = target - 1;
    for (int i = k; i < n; ++i) {
      cur = ((cur << 1) & full) | s[i] - '0';
      st.emplace(cur);
      if (st.size() == target) {
        return true;
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
  string s = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.hasAllCodes(s, k);
}
