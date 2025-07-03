//go:build ignore
#include "cpp/common/Solution.h"
#include <cmath>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  vector<int> bestCoordinate(const vector<vector<int>> &towers, int radius) {
    int ans = 0;
    int ans_x = 0, ans_y = 0;
    radius *= radius;
    for (int x = 0; x <= 50; ++x) {
      for (int y = 0; y <= 50; ++y) {
        int total = 0;
        for (const auto &tower : towers) {
          int tx = tower[0], ty = tower[1], q = tower[2];
          int d = (tx - x) * (tx - x) + (ty - y) * (ty - y);
          if (d <= radius) {
            total += floor(q / (1 + sqrt(d)));
          }
        }
        if (total > ans) {
          ans = total;
          ans_x = x;
          ans_y = y;
        }
      }
    }
    return {ans_x, ans_y};
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
  vector<vector<int>> towers = json::parse(inputArray.at(0));
  int radius = json::parse(inputArray.at(1));
  return solution.bestCoordinate(towers, radius);
}
