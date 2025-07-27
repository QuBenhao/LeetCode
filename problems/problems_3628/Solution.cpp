//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long numOfSubsequences(const string &s) {
    int n = s.size();
    vector<int> suf_t(n + 1, 0);
    vector<int> suf_c(n + 1, 0);
    for (int i = n - 1; i >= 0; --i) {
      suf_t[i] = suf_t[i + 1];
      suf_c[i] = suf_c[i + 1];
      if (s[i] == 'T') {
        ++suf_t[i];
      } else if (s[i] == 'C') {
        suf_c[i] += suf_t[i + 1];
      }
    }
    int64_t ans = 0, max_add = 0;
    int pre_l = 0, pre_c = 0;
    for (int i = 0; i < n; ++i) {
      if (s[i] == 'L') {
        ++pre_l;
        ans += suf_c[i];
      } else if (s[i] == 'C') {
        pre_c += pre_l;
      }
      if (max_add < suf_c[i]) {
        max_add = suf_c[i];
      }
      max_add = max(max_add, static_cast<int64_t>(pre_l) * suf_t[i]);
      if (max_add < pre_c) {
        max_add = pre_c;
      }
    }
    return ans + max_add;
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
  return solution.numOfSubsequences(s);
}
