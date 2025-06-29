//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> longestCommonPrefix(vector<string> &words) {
    auto get_cp = [&words](int i, int j) {
      int k = 0;
      while (k < words[i].size() && k < words[j].size() &&
             words[i][k] == words[j][k]) {
        ++k;
      }
      return k;
    };

    int n = words.size();
    if (n == 1) {
      return {0};
    }
    vector<int> cps(n, 0);
    for (int i = 0; i < n - 1; ++i) {
      cps[i + 1] = get_cp(i, i + 1);
    }
    vector<int> suffix(n, 0);
    for (int i = n - 2; i >= 0; --i) {
      suffix[i] = max(suffix[i + 1], cps[i + 1]);
    }
    int prefix = 0;
    vector<int> ans(n, 0);
    ans[0] = suffix[1];
    for (int i = 1; i < n - 1; ++i) {
      ans[i] = max(max(prefix, suffix[i + 1]), get_cp(i - 1, i + 1));
      prefix = max(prefix, cps[i]);
    }
    ans[n - 1] = prefix;
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
  vector<string> words = json::parse(inputArray.at(0));
  return solution.longestCommonPrefix(words);
}
