//go:build ignore
#include "cpp/common/Solution.h"

#include <algorithm>

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  long long kthSmallestProduct(const vector<int> &nums1,
                               const vector<int> &nums2, long long k) {
    int64_t m = nums1.size(), n = nums2.size();
    int64_t zero1 = lower_bound(nums1.begin(), nums1.end(), 0) - nums1.begin();
    int64_t zero2 = lower_bound(nums2.begin(), nums2.end(), 0) - nums2.begin();

    auto count = [&](int64_t x) {
      int64_t count;
      if (x < 0) {
        count = 0;
        int64_t i = zero1, j = 0;
        while (i < m && j < zero2) {
          if ((int64_t)nums1[i] * nums2[j] > x) {
            ++i;
          } else {
            count += m - i;
            ++j;
          }
        }
        i = 0, j = zero2;
        while (i < zero1 && j < n) {
          if ((int64_t)nums1[i] * nums2[j] > x) {
            ++j;
          } else {
            count += n - j;
            ++i;
          }
        }
      } else {
        count = zero1 * (n - zero2) + zero2 * (m - zero1);
        int64_t i = 0, j = zero2 - 1;
        while (i < zero1 && j >= 0) {
          if ((int64_t)nums1[i] * nums2[j] > x) {
            ++i;
          } else {
            count += zero1 - i;
            --j;
          }
        }
        i = zero1, j = n - 1;
        while (i < m && j >= zero2) {
          if ((int64_t)nums1[i] * nums2[j] > x) {
            --j;
          } else {
            count += j - zero2 + 1;
            ++i;
          }
        }
      }
      return count >= k;
    };

    array<int64_t, 4> corners = {
        (int64_t)nums1[0] * nums2[0], (int64_t)nums1[m - 1] * nums2[n - 1],
        (int64_t)nums1[0] * nums2[n - 1], (int64_t)nums1[m - 1] * nums2[0]};
    int64_t left = *min_element(corners.begin(), corners.end());
    int64_t right = *max_element(corners.begin(), corners.end());
    while (left < right) {
      int64_t mid = left + (right - left) / 2;
      if (count(mid)) {
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
  vector<int> nums1 = json::parse(inputArray.at(0));
  vector<int> nums2 = json::parse(inputArray.at(1));
  long long k = json::parse(inputArray.at(2));
  return solution.kthSmallestProduct(nums1, nums2, k);
}
