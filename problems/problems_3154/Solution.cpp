//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

int c[31][31];

auto init = [] {
  for (int i = 0; i < 31; i++) {
    c[i][0] = c[i][i] = 1;
    for (int j = 1; j < i; j++) {
      c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
    }
  }
  return 0;
}();

class Solution {
public:
  int waysToReachStair(int k) {
    int ans = 0;
    for (int j = 0; j < 30; j++) {
      int m = (1 << j) - k;
      if (0 <= m && m <= j + 1) {
        ans += c[j + 1][m];
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
  int k = json::parse(inputArray.at(0));
  return solution.waysToReachStair(k);
}
