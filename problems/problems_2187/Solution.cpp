//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int64_t minimumTime(vector<int> &time, int totalTrips) {
    auto check = [&](int64_t x) -> bool {
      int64_t sum = 0;
      for (int t : time) {
        sum += x / t;
        if (sum >= totalTrips) {
          return true;
        }
      }
      return false;
    };

    auto [min_t, max_t] = ranges::minmax(time);
    int avg = (totalTrips - 1) / time.size() + 1;
    // 循环不变量：check(left) 恒为 false
    int64_t left = (int64_t)min_t * avg - 1;
    // 循环不变量：check(right) 恒为 true
    int64_t right =
        min((int64_t)max_t * avg, (int64_t)min_t * totalTrips);
    while (left + 1 < right) {  // 开区间 (left, right) 不为空
      int64_t mid = (left + right) / 2;
      (check(mid) ? right : left) = mid;
    }
    // 此时 left 等于 right-1
    // check(left) = false 且 check(right) = true，所以答案是 right
    return right;  // 最小的 true
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
  vector<int> time = json::parse(inputArray.at(0));
  int totalTrips = json::parse(inputArray.at(1));
  return solution.minimumTime(time, totalTrips);
}
