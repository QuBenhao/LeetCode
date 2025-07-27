//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const int MAX_N = 1000001;
vector<int> prime_factors[MAX_N];
bool inited = false;
void init() {
  if (inited) {
    return;
  }
  inited = true;
  for (int i = 2; i < MAX_N; ++i) {
    if (prime_factors[i].empty()) {
      for (int j = i; j < MAX_N; j += i) {
        prime_factors[j].push_back(i);
      }
    }
  }
}

class Solution {
public:
  int minJumps(const vector<int> &nums) {
    init();
    unordered_map<int, vector<int>> graph;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
      for (int p : prime_factors[nums[i]]) {
        graph[p].push_back(i);
      }
    }
    vector<int> q{0};
    vector<bool> visited(n, false);
    visited[0] = true;
    int steps = 0;
    while (!q.empty()) {
      vector<int> next_q;
      for (int i : q) {
        if (i == n - 1) {
          return steps;
        }
        auto &idxes = graph[nums[i]];
        idxes.push_back(i + 1);
        if (i > 0) {
          idxes.push_back(i - 1);
        }
        for (int j : idxes) {
          if (!visited[j]) {
            visited[j] = true;
            next_q.push_back(j);
          }
        }
        idxes.clear();  // Clear to avoid reprocessing
      }
      q = std::move(next_q);
      ++steps;
    }
    return -1;
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
  return solution.minJumps(nums);
}
