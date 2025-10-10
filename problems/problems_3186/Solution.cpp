//go:build ignore
#include "cpp/common/Solution.h"
#include <iterator>
#include <map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long maximumTotalDamage(const vector<int> &power) {
    map<int, int> counts;
    for (const auto &p : power) {
      ++counts[p];
    }
    int n = counts.size();
    vector<int64_t> dp(n + 1);
    int idx = 0, j_idx = 0;
    for (auto i = counts.begin(), j = counts.begin(); i != counts.end();
         ++idx, i = next(i)) {
      int64_t cur = i->first;
      while (j->first < cur - 2) {
        j = next(j);
        ++j_idx;
      }
      dp[idx + 1] = max(dp[idx], dp[j_idx] + cur * i->second);
    }
    return dp[n];
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
  vector<int> power = json::parse(inputArray.at(0));
  return solution.maximumTotalDamage(power);
}
