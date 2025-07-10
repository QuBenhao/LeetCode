//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int countDays(int days, vector<vector<int>> &meetings) {
    sort(
        meetings.begin(), meetings.end(),
        [](const auto &a, const auto &b) { return a[0] < b[0]; });
    int ans = 0, cur = 0;
    for (const auto &meeting : meetings) {
      int start = meeting[0], end = meeting[1];
      if (start > cur) {
        ans += start - cur - 1;
      }
      cur = max(cur, end);
    }
    return ans + days - cur;
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
  int days = json::parse(inputArray.at(0));
  vector<vector<int>> meetings = json::parse(inputArray.at(1));
  return solution.countDays(days, meetings);
}
