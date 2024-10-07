//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minSpeedOnTime(vector<int> &dist, double hour) {
    int n = dist.size();
    if (hour <= n - 1) {
      return -1;
    }
    int left = 1, right = 1e7;
    while (left < right) {
      int mid = left + (right - left) / 2;
      double time = 0;
      for (int i = 0; i < n - 1; ++i) {
        time += (dist[i] + mid - 1) / mid;
      }
      time += 1.0 * dist[n - 1] / mid;
      if (time > hour) {
        left = mid + 1;
      } else {
        right = mid;
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
  vector<int> dist = json::parse(inputArray.at(0));
  double hour = json::parse(inputArray.at(1));
  return solution.minSpeedOnTime(dist, hour);
}
