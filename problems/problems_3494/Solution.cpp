//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long minTime(const vector<int> &skill, const vector<int> &mana) {
    int n = skill.size(), m = mana.size();
    vector<int> s(n + 1);  // skill 的前缀和
    partial_sum(skill.begin(), skill.end(), s.begin() + 1);

    int64_t start = 0;
    for (int j = 1; j < m; j++) {
      int64_t mx = 0;
      for (int i = 0; i < n; i++) {
        mx = max(mx, 1LL * mana[j - 1] * s[i + 1] - 1LL * mana[j] * s[i]);
      }
      start += mx;
    }
    return start + 1LL * mana[m - 1] * s[n];
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
  vector<int> skill = json::parse(inputArray.at(0));
  vector<int> mana = json::parse(inputArray.at(1));
  return solution.minTime(skill, mana);
}
