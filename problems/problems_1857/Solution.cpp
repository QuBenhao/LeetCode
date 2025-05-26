//go:build ignore
#include "cpp/common/Solution.h"

#include <deque>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int largestPathValue(string colors, vector<vector<int>> &edges) {
    size_t n = colors.length();
    vector<vector<int>> graph(n);
    vector<int> indegree(n, 0);
    for (auto edge : edges) {
      graph[edge[0]].push_back(edge[1]);
      indegree[edge[1]]++;
    }
    deque<int> queue;
    vector<vector<int>> count(n, vector<int>(26, 0));
    for (size_t i = 0; i < n; i++) {
      if (indegree[i] == 0) {
        queue.push_back(i);
      }
    }
    int ans = 0;
    size_t c = 0;
    while (!queue.empty()) {
      auto node = queue.front();
      queue.pop_front();
      c++;
      ans = max(ans, ++count[node][colors[node] - 'a']);
      for (auto child : graph[node]) {
        for (int i = 0; i < 26; i++) {
          count[child][i] = max(count[child][i], count[node][i]);
        }
        indegree[child]--;
        if (indegree[child] == 0) {
          queue.push_back(child);
        }
      }
    }
    if (c < n) {
      return -1;
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
  string colors = json::parse(inputArray.at(0));
  vector<vector<int>> edges = json::parse(inputArray.at(1));
  return solution.largestPathValue(colors, edges);
}
