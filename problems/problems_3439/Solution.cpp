//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxFreeTime(int eventTime, int k, const vector<int> &startTime,
                  const vector<int> &endTime) {
    int n = startTime.size();

    auto getDistance = [&](int idx) {
      if (idx == 0) {
        return startTime[0];
      } else if (idx == n) {
        return eventTime - endTime[n - 1];
      } else {
        return startTime[idx] - endTime[idx - 1];
      }
    };

    int cur = 0;
    for (int i = 0; i <= k; ++i) {
      cur += getDistance(i);
    }
    int ans = cur;
    for (int i = k + 1; i <= n; ++i) {
      cur += getDistance(i) - getDistance(i - k - 1);
      ans = max(ans, cur);
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
  int eventTime = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  vector<int> startTime = json::parse(inputArray.at(2));
  vector<int> endTime = json::parse(inputArray.at(3));
  return solution.maxFreeTime(eventTime, k, startTime, endTime);
}
