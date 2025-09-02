//go:build ignore
#include "cpp/common/Solution.h"
#include <cstdint>
#include <vector>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int numberOfPairs(vector<vector<int>> &points) {
    ranges::sort(points, {}, [](auto& p) {return pair{p[0], -p[1]}; });
    int ans = 0;
    for (int i = 0, n = points.size(); i < n; ++i) {
      int max_y = INT32_MIN;
      for (int j = i + 1; j < n; ++j) {
        if (points[i][1] >= points[j][1] && points[j][1] > max_y) {
          max_y = points[j][1];
          ++ans;
          if (max_y == points[i][1]) {
            break;
          }
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
