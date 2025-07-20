//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

const int MOD = 1'000'000'007;

class Solution {
public:
  int countTrapezoids(const vector<vector<int>> &points) {
    unordered_map<int, int> group_y;
    for (const auto &point : points) {
      ++group_y[point[1]];
    }
    int64_t ans = 0;
    int64_t s = 0;
    for (const auto &[_, v] : group_y) {
      int64_t k = 1LL * v * (v - 1) / 2 % MOD;
      ans = (k * s % MOD + ans) % MOD;
      s = (k + s) % MOD;
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
