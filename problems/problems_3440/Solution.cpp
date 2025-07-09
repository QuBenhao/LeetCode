//go:build ignore
#include "cpp/common/Solution.h"
#include <utility>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxFreeTime(int eventTime, const vector<int> &startTime,
                  const vector<int> &endTime) {
    int n = startTime.size();
    vector<int> distances(n + 1);
    distances[0] = startTime[0];
    for (int i = 1; i < n; ++i) {
      distances[i] = startTime[i] - endTime[i - 1];
    }
    distances[n] = eventTime - endTime[n - 1];

    vector<int>::const_iterator a = distances.end(), b = distances.end(),
                                c = distances.end();
    for (auto it = distances.begin(); it != distances.end(); ++it) {
      if (a == distances.end() || *it >= *a) {
        swap(b, c);
        swap(a, b);
        a = it;
      } else if (b == distances.end() || *it >= *b) {
        swap(c, b);
        b = it;
      } else if (c == distances.end() || *it > *c) {
        c = it;
      }
    }
    int ia = a - distances.begin(), ib = b - distances.begin();

    auto getMax = [&a, &b, &c, ia, ib](int x) {
      if (x != ia && x + 1 != ia) {
        return *a;
      }
      if (x != ib && x + 1 != ib) {
        return *b;
      }
      return *c;
    };

    int ans = 0;
    for (int i = 0; i < n; ++i) {
      int cur = endTime[i] - startTime[i];
      if (getMax(i) >= cur) {
        ans = max(ans, distances[i] + distances[i + 1] + cur);
      } else {
        ans = max(ans, distances[i] + distances[i + 1]);
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
  int eventTime = json::parse(inputArray.at(0));
  vector<int> startTime = json::parse(inputArray.at(1));
  vector<int> endTime = json::parse(inputArray.at(2));
  return solution.maxFreeTime(eventTime, startTime, endTime);
}
