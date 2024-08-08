//go:build ignore
#include "cpp/common/Solution.h"
#include <deque>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maximumRobots(vector<int> &chargeTimes, vector<int> &runningCosts,
                    long long budget) {
    int n = static_cast<int>(chargeTimes.size());
    int left = 0, right = n;
    auto check = [&](int len) -> bool {
      long long s = 0;
      deque<int> q;
      for (int i = 0; i < n; i++) {
        while (!q.empty() && chargeTimes[q.back()] <= chargeTimes[i]) {
          q.pop_back();
        }
        q.push_back(i);
        s += runningCosts[i];
        if (i >= q.front() + len) {
          q.pop_front();
        }
        if (i >= len - 1) {
          if (s * len + chargeTimes[q.front()] <= budget) {
            return true;
          }
          s -= runningCosts[i - len + 1];
        }
      }
      return false;
    };
    while (left < right) {
      int mid = left + (right - left + 1) / 2;
      if (check(mid)) {
        left = mid;
      } else {
        right = mid - 1;
      }
    }
    return left;
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
  vector<int> chargeTimes = json::parse(inputArray.at(0));
  vector<int> runningCosts = json::parse(inputArray.at(1));
  long long budget = json::parse(inputArray.at(2));
  return solution.maximumRobots(chargeTimes, runningCosts, budget);
}
