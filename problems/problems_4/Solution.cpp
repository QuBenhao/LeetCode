//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
    int m = static_cast<int>(nums1.size()), n = static_cast<int>(nums2.size());
    function<int(int, int, int)> getKthElement = [&](int k, int start1,
                                                     int start2) -> int {
      if (m - start1 > n - start2) {
        swap(m, n);
        swap(nums1, nums2);
        swap(start1, start2);
      }
      if (m == start1) {
        return nums2[start2 + k - 1];
      }
      if (k == 1) {
        return min(nums1[start1], nums2[start2]);
      }
      int ni = min(start1 + k / 2, m), nj = start2 + k - (ni - start1);
      if (nums1[ni - 1] > nums2[nj - 1]) {
        return getKthElement(k - (nj - start2), start1, nj);
      } else {
        return getKthElement(k - (ni - start1), ni, start2);
      }
    };
    int totalLength = m + n;
    if (totalLength % 2 == 1) {
      return static_cast<double>(getKthElement(totalLength / 2 + 1, 0, 0));
    } else {
      return (getKthElement(totalLength / 2, 0, 0) +
              getKthElement(totalLength / 2 + 1, 0, 0)) /
             2.0;
    }
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
  return solution.findMedianSortedArrays(nums1, nums2);
}
