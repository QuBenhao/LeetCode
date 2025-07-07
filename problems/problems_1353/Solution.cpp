//go:build ignore
#include "cpp/common/Solution.h"
#include <functional>
#include <queue>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxEvents(vector<vector<int>> &events) {
    sort(events.begin(), events.end());
    int n = events.size();
    int ans = 0;
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int i = 0, cur = events[0][0]; i < n || !pq.empty();) {
      while (i < n && events[i][0] <= cur) {
        pq.push(events[i][1]);
        ++i;
      }
      if (!pq.empty()) {
        ++ans;
        ++cur;
        pq.pop();
        while (!pq.empty() && pq.top() < cur) {
          pq.pop();
        }
      } else {
        cur = events[i][0];
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
  vector<vector<int>> events = json::parse(inputArray.at(0));
  return solution.maxEvents(events);
}
