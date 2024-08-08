//go:build ignore
#include "cpp/common/Solution.h"
#include <deque>
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  bool canFinish(int numCourses, vector<vector<int>> &prerequisites) {
    vector<int> degree(numCourses, 0);
    unordered_map<int, vector<int>> graph;
    for (auto req : prerequisites) {
      degree[req[0]]++;
      graph[req[1]].emplace_back(req[0]);
    }
    deque<int> q;
    for (int i = 0; i < numCourses; i++) {
      if (degree[i] == 0) {
        q.emplace_back(i);
      }
    }
    int explored = 0;
    while (!q.empty()) {
      int first = q.front();
      q.pop_front();
      explored++;
      for (auto other : graph[first]) {
        if (--degree[other] == 0) {
          q.emplace_back(other);
        }
      }
    }
    return explored == numCourses;
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
  return solution.canFinish(numCourses, prerequisites);
}
