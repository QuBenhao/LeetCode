//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
public:
  int minimumAddedInteger(vector<int> &nums1, vector<int> &nums2) {
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    int i = 2;
  out:
    while (i >= 0) {
      int diff = nums2[0] - nums1[i], quota = 2 - i, idx = i + 1;
      for (int j = 1; j < static_cast<int>(nums2.size()); j++) {
        while (nums2[j] - nums1[idx] != diff) {
          if (quota-- == 0) {
            i--;
            goto out;
          }
          idx++;
        }
        idx++;
      }
      return diff;
    }
    return nums2[0] - nums1[0];
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
  return solution.minimumAddedInteger(nums1, nums2);
}
