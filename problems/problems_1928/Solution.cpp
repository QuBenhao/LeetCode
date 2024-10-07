//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
private:
  // 极大值
  static constexpr int INFTY = INT_MAX / 2;

public:
  int minCost(int maxTime, vector<vector<int>> &edges,
              vector<int> &passingFees) {
    int n = passingFees.size();
    vector<vector<int>> f(maxTime + 1, vector<int>(n, INFTY));
    f[0][0] = passingFees[0];
    for (int t = 1; t <= maxTime; ++t) {
      for (const auto &edge : edges) {
        int i = edge[0], j = edge[1], cost = edge[2];
        if (cost <= t) {
          f[t][i] = min(f[t][i], f[t - cost][j] + passingFees[i]);
          f[t][j] = min(f[t][j], f[t - cost][i] + passingFees[j]);
        }
      }
    }

    int ans = INFTY;
    for (int t = 1; t <= maxTime; ++t) {
      ans = min(ans, f[t][n - 1]);
    }
    return ans == INFTY ? -1 : ans;
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
  int maxTime = json::parse(inputArray.at(0));
  vector<vector<int>> edges = json::parse(inputArray.at(1));
  vector<int> passingFees = json::parse(inputArray.at(2));
  return solution.minCost(maxTime, edges, passingFees);
}
