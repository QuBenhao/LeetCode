//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  double largestTriangleArea(const vector<vector<int>> &points) {
    double ans = 0.0;
    for (int i = 0, n = points.size(); i < n - 2; ++i) {
      for (int j = i + 1; j < n - 1; ++j) {
        for (int k = j + 1; k < n; ++k) {
          int x1 = points[i][0], y1 = points[i][1];
          int x2 = points[j][0], y2 = points[j][1];
          int x3 = points[k][0], y3 = points[k][1];
          ans = max(ans, abs((x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 -
                              x3 * y2) /
                             2.0));
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
  return solution.largestTriangleArea(points);
}
