//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> successfulPairs(const vector<int> &spells,
                              const vector<int> &potions, long long success) {
    int n = spells.size();
    vector<int> ans(n, 0);
    int max = *max_element(potions.begin(), potions.end());
    vector<int> counts(max + 1);
    for (const auto &p : potions) {
      ++counts[p];
    }
    for (int i = max - 1; i >= 0; --i) {
      counts[i] += counts[i + 1];
    }
    for (int i = 0; i < n; ++i) {
      int64_t need = (success - 1) / spells[i] + 1;
      if (need > max) {
        continue;
      }
      ans[i] = counts[need];
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
  vector<int> spells = json::parse(inputArray.at(0));
  vector<int> potions = json::parse(inputArray.at(1));
  long long success = json::parse(inputArray.at(2));
  return solution.successfulPairs(spells, potions, success);
}
