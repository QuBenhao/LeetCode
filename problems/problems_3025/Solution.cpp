//go:build ignore
#include "cpp/common/Solution.h"
#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int numberOfPairs(vector<vector<int>> &points) {
    ranges::sort(points, [](const vector<int> &p1, const vector<int> &p2) {
      if (p1[0] != p2[0]) {
        return p1[0] < p2[0];
      }
      return p2[1] < p1[1];
    });
    int ans = 0, n = points.size();
    for (int i = 0; i < n; ++i) {
      int max_y = -1;
      for (int j = i + 1; j < n; ++j) {
        if (points[i][1] >= points[j][1] && points[j][1] > max_y) {
          max_y = points[j][1];
          ++ans;
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
  vector<vector<int>> points = json::parse(inputArray.at(0));
  return solution.numberOfPairs(points);
}
