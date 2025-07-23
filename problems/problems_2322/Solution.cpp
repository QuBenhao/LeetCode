//go:build ignore
#include "cpp/common/Solution.h"
#include <cstdint>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumScore(const vector<int> &nums, const vector<vector<int>> &edges) {
    int n = nums.size();
    vector<vector<int>> graph(n);
    for (const auto &edge : edges) {
      int u = edge[0], v = edge[1];
      graph[u].push_back(v);
      graph[v].push_back(u);
    }

    vector<int> xors(n, 0);
    vector<int> time_in(n, 0);
    vector<int> time_out(n, 0);
    int timer = 0;
    auto dfs = [&](this auto &&dfs, int node, int parent) -> int {
      xors[node] = nums[node];
      time_in[node] = ++timer;
      for (int neighbor : graph[node]) {
        if (neighbor != parent) {
          xors[node] ^= dfs(neighbor, node);
        }
      }
      time_out[node] = ++timer;
      return xors[node];
    };
    dfs(0, -1);
    int ans = INT32_MAX;
    for (int x = 1; x < n - 1; ++x) {
      for (int y = x + 1; y < n; ++y) {
        int a, b, c;
        if (time_in[x] < time_in[y] && time_in[y] < time_out[x]) {
          a = xors[y];
          b = xors[x] ^ a;
          c = xors[0] ^ xors[x];
        } else if (time_in[y] < time_in[x] && time_in[x] < time_out[y]) {
          a = xors[x];
          b = xors[y] ^ a;
          c = xors[0] ^ xors[y];
        } else {
          a = xors[x];
          b = xors[y];
          c = xors[0] ^ (a ^ b);
        }
        ans = min(ans, max({a, b, c}) - min({a, b, c}));
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
  vector<int> nums = json::parse(inputArray.at(0));
  vector<vector<int>> edges = json::parse(inputArray.at(1));
  return solution.minimumScore(nums, edges);
}
