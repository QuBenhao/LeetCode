//go:build ignore
#include "cpp/common/Solution.h"
#include <queue>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> findOrder(int numCourses,
                        const vector<vector<int>> &prerequisites) {
    vector<int> degree(numCourses);
    vector<vector<int>> children(numCourses);
    for (const auto &prerequisity : prerequisites) {
      ++degree[prerequisity[0]];
      children[prerequisity[1]].emplace_back(prerequisity[0]);
    }
    queue<int> q;
    for (int i = 0; i < numCourses; ++i) {
      if (degree[i] == 0) {
        q.push(i);
      }
    }
    vector<int> ans(numCourses);
    int idx = 0;
    while (!q.empty()) {
      int node = q.front();
      ans[idx++] = node;
      q.pop();
      for (const auto &child : children[node]) {
        if (--degree[child] == 0) {
          q.push(child);
        }
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
  int numCourses = json::parse(inputArray.at(0));
  vector<vector<int>> prerequisites = json::parse(inputArray.at(1));
  return solution.findOrder(numCourses, prerequisites);
}
