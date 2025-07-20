//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int countTrapezoids(const vector<vector<int>> &points) {
    unordered_map<double, unordered_map<double, int>>
        cnt;                                              // 斜率 -> 截距 -> 个数
    unordered_map<int, unordered_map<double, int>> cnt2;  // 中点 -> 斜率 -> 个数
    int n = points.size();
    for (int i = 0; i < n - 1; ++i) {
      int x1 = points[i][0], y1 = points[i][1];
      for (int j = i + 1; j < n; ++j) {
        int x2 = points[j][0], y2 = points[j][1];
        double k, b;
        if (x1 == x2) {
          k = 1e9;
          b = x1;
        } else {
          k = 1.0 * (y2 - y1) / (x2 - x1);
          b = 1.0 * (y1 * (x2 - x1) - x1 * (y2 - y1)) / (x2 - x1);
        }
        ++cnt[k][b];
        int mask = (x1 + x2 + 2000) << 16 | (y1 + y2 + 2000);
        ++cnt2[mask][k];
      }
    }
    int ans = 0;
    for (const auto &[_, m] : cnt) {
      int s = 0;
      for (const auto &[_, v] : m) {
        ans += s * v;
        s += v;
      }
    }
    for (const auto &[_, m] : cnt2) {
      int s = 0;
      for (const auto &[_, v] : m) {
        ans -= s * v;
        s += v;
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
  return solution.countTrapezoids(points);
}
