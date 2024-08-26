//go:build ignore
#include "cpp/common/Solution.h"
#include <unordered_map>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int medianOfUniquenessArray(vector<int> &nums) {
    int n = static_cast<int>(nums.size());
    long long k = (static_cast<long long>(n) * (n + 1) / 2 + 1) / 2;

    auto check = [&](int x) {
      long long cnt = 0;
      unordered_map<int, int> freq;
      for (int l = 0, r = 0; r < n; r++) {
        freq[nums[r]]++;
        while (freq.size() > x) {
          freq[nums[l]]--;
          if (freq[nums[l]] == 0) {
            freq.erase(nums[l]);
          }
          l++;
        }
        cnt += static_cast<long long>(r) - l + 1;
        if (cnt >= k) {
          return true;
        }
      }
      return false;
    };

    int left = 1, right = n;
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
  return solution.medianOfUniquenessArray(nums);
}
