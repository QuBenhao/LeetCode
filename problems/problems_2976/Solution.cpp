//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>
#include <utility>
#include <vector>

using namespace std;
using json = nlohmann::json;

constexpr long long INF = 0x3f3f3f3f;

class Solution {
public:
  long long minimumCost(const string& source, const string& target, const vector<char> &original,
                        const vector<char> &changed, const vector<int> &cost) {
    vector trans(26, vector<int64_t>(26, INF));
    for (int i = 0; i < 26; ++i) {
      trans[i][i] = 0;
    }
    deque<pair<int, int>> q;
    for (size_t i = 0; i < original.size(); ++i) {
      int a = original[i] - 'a', b = changed[i] - 'a';
      if (trans[a][b] > cost[i]) {
        trans[a][b] = cost[i];
        q.emplace_back(a, b);
      }
    }
    while (!q.empty()) {
      auto [a, b] = q.front();
      q.pop_front();
      for (int other = 0; other < 26; ++other) {
        if (other == a || other == b)
          continue;
        if (int64_t nc = trans[other][a] + trans[a][b]; nc < trans[other][b]) {
          trans[other][b] = nc;
          q.emplace_back(other, b);
        }
      }
    }
    long long ans = 0LL;
    for (size_t i = 0; i < source.size(); ++i) {
      if (source[i] == target[i])
        continue;
      int a = source[i] - 'a', b = target[i] - 'a';
      if (trans[a][b] == INF)
        return -1;
      ans += trans[a][b];
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
  string source = json::parse(inputArray.at(0));
  string target = json::parse(inputArray.at(1));
  vector<string> original_str = json::parse(inputArray.at(2));
  auto original = vector<char>(original_str.size());
  for (size_t i = 0; i < original.size(); ++i) {
    original[i] = original_str[i][0];
  }
  vector<string> changed_str = json::parse(inputArray.at(3));
  auto changed = vector<char>(changed_str.size());
  for (size_t i = 0; i < changed.size(); ++i) {
    changed[i] = changed_str[i][0];
  }
  vector<int> cost = json::parse(inputArray.at(4));
  return solution.minimumCost(source, target, original, changed, cost);
}
