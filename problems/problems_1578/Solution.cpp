//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minCost(const string &colors, const vector<int> &neededTime) {
    int ans = 0, n = colors.length();
    for (int i = 0, j = 0; i < n - 1; i = j) {
      for (j = i + 1; j < n && colors[j] == colors[i]; ++j) {
        if (neededTime[i] < neededTime[j]) {
          ans += neededTime[i];
          i = j;
        } else {
          ans += neededTime[j];
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
  string colors = json::parse(inputArray.at(0));
  vector<int> neededTime = json::parse(inputArray.at(1));
  return solution.minCost(colors, neededTime);
}
