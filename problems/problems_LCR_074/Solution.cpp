//go:build ignore
#include "cpp/common/Solution.h"
#include "cpp/models/TreeNode.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<vector<int>> merge(vector<vector<int>> &intervals) {
    sort(
        intervals.begin(), intervals.end(),
        [](const vector<int> &a, const vector<int> &b) { return a[0] < b[0]; });
    vector<vector<int>> ans = {intervals[0]};
    for (auto interval : intervals) {
      if (interval[0] <= ans.back()[1]) {
        ans.back()[1] = max(ans.back()[1], interval[1]);
      } else {
        ans.push_back(interval);
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
  vector<vector<int>> intervals = json::parse(inputArray.at(0));
  return solution.merge(intervals);
}
