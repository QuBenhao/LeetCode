//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minSwaps(vector<int> &nums) {
    array<vector<int>, 2> values;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
      values[nums[i] & 1].push_back(i);
    }
    auto swap = [&values, n](int start) {
      int count = 0;
      const auto &arr = values[start];
      for (int i = 0, idx = 0; i < n; i += 2) {
        count += abs(arr[idx++] - i);
      }
      return count;
    };
    int even_size = values[0].size(), odd_size = values[1].size();
    if (abs(even_size - odd_size) > 1) {
      return -1;
    }
    int ans = INT_MAX;
    if (even_size >= odd_size) {
      ans = min(ans, swap(0));
    }
    if (odd_size >= even_size) {
      ans = min(ans, swap(1));
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
  vector<int> nums = json::parse(inputArray.at(0));
  return solution.minSwaps(nums);
}
