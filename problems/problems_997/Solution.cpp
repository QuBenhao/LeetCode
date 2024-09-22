//go:build ignore
#include "cpp/common/Solution.h"
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int findJudge(int n, vector<vector<int>> &trust) {
    vector<int> counter(n + 1, 0);
    for (auto &t : trust) {
      counter[t[0]]--;
      counter[t[1]]++;
    }
    for (int i = 1; i <= n; i++) {
      if (counter[i] == n - 1) {
        return i;
      }
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
  int n = json::parse(inputArray.at(0));
  vector<vector<int>> trust = json::parse(inputArray.at(1));
  return solution.findJudge(n, trust);
}
