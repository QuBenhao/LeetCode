//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int edgeScore(vector<int> &edges) {
    int ans = 0, n = static_cast<int>(edges.size());
    vector<int64_t> counter(n, 0);
    for (int i = 0; i < n; i++) {
      counter[edges[i]] += i;
      if (counter[edges[i]] > counter[ans]) {
        ans = edges[i];
      } else if (counter[edges[i]] == counter[ans]) {
        ans = min(ans, edges[i]);
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
  vector<int> edges = json::parse(inputArray.at(0));
  return solution.edgeScore(edges);
}
