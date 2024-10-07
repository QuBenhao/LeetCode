//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
private:
  void dfs(vector<vector<int>> &graph, int node, vector<int> &path,
           vector<vector<int>> &res) {
    path.push_back(node);
    if (node == graph.size() - 1) {
      res.push_back(path);
    } else {
      for (int nextNode : graph[node]) {
        dfs(graph, nextNode, path, res);
      }
    }
    path.pop_back();
  }

public:
  vector<vector<int>> allPathsSourceTarget(vector<vector<int>> &graph) {
    vector<vector<int>> res;
    vector<int> path;
    dfs(graph, 0, path, res);
    return res;
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
  vector<vector<int>> graph = json::parse(inputArray.at(0));
  return solution.allPathsSourceTarget(graph);
}
