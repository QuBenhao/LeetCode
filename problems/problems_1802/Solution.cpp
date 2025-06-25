//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int maxValue(int n, int index, int maxSum) {
    int left = 1, right = maxSum - n + 1;
    auto check = [n, index, maxSum](int mid) {
      int64_t leftSum = 0, rightSum = 0;
      // 从0到index-1
      if (mid > index) {
        leftSum = (int64_t)(mid - 1 + mid - index) * index / 2;
      } else {
        leftSum = (int64_t)(mid - 1 + 1) * (mid - 1) / 2 + (index - mid + 1);
      }
      // 从index+1到n-1
      if (mid > n - index - 1) {
        rightSum =
            (int64_t)(mid - 1 + mid - (n - index - 1)) * (n - index - 1) / 2;
      } else {
        rightSum = (int64_t)(mid - 1 + 1) * (mid - 1) / 2 +
                   ((n - index - 1) - mid + 1);
      }
      return leftSum + rightSum <= maxSum - mid;
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
  int n = json::parse(inputArray.at(0));
  int index = json::parse(inputArray.at(1));
  int maxSum = json::parse(inputArray.at(2));
  return solution.maxValue(n, index, maxSum);
}
