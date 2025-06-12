//go:build ignore
#include "cpp/common/Solution.h"
#include <cstdint>
#include <numeric>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long maxGCDScore(vector<int> &nums, int k) {
    int64_t ans = 0;
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
      int lb_min = INT32_MAX, used = 0, g = 0;
      for (int j = i; j >= 0; --j) {
        int x = nums[j];
        int lb = x & -x;
        if (lb < lb_min) {
          lb_min = lb;
          used = 1;
        } else if (lb == lb_min) {
          ++used;
        }
        g = gcd(g, x);
        int64_t new_g = g;
        if (used <= k) {
          new_g *= 2;
        }
        int64_t s = new_g * (1LL + i - j);
        if (s > ans) {
          ans = s;
        }
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
  vector<int> nums = json::parse(inputArray.at(0));
  int k = json::parse(inputArray.at(1));
  return solution.maxGCDScore(nums, k);
}
