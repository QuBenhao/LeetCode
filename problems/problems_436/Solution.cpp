//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> findRightInterval(vector<vector<int>> &intervals) {
    unordered_map<int, int> indexMap;
    int n = intervals.size();
    for (int i = 0; i < n; ++i) {
      indexMap[intervals[i][0]] = i;
    }
    vector<int> result(n, -1);
    sort(
        intervals.begin(), intervals.end(),
        [](const vector<int> &a, const vector<int> &b) { return a[0] < b[0]; });
    for (int i = 0; i < n; ++i) {
      auto it =
          lower_bound(intervals.begin(), intervals.end(), intervals[i][1],
                      [](const vector<int> &a, int val) { return a[0] < val; });
      if (it != intervals.end()) {
        int index = it - intervals.begin();
        result[indexMap[intervals[i][0]]] = indexMap[intervals[index][0]];
      }
    }
    return result;
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
  return solution.findRightInterval(intervals);
}
