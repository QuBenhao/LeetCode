//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimizeMax(vector<int> &nums, int p) {
    sort(nums.begin(), nums.end());
    auto check = [&](int x) {
      int count = 0;
      for (int i = 0; i < nums.size() - 1 && count < p; ++i) {
        if (nums[i + 1] - nums[i] <= x) {
          ++count;
          ++i;  // Skip the next element as it's paired with the current one
        }
      }
      return count >= p;
    };
    int left = 0, right = nums.back() - nums.front();
    while (left < right) {
      int mid = left + (right - left) / 2;
      if (check(mid)) {
        right = mid;
      } else {
        left = mid + 1;
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
  vector<int> nums = json::parse(inputArray.at(0));
  int p = json::parse(inputArray.at(1));
  return solution.minimizeMax(nums, p);
}
