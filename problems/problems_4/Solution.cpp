//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
    int find_k_smallest(vector<int>& nums1, int i, vector<int>& nums2, int j, int k) {
        // Find the kth smallest number in two sorted arrays
        if (nums1.size() - i > nums2.size() - j) { // Swap to ensure nums1 has fewer available numbers and nums2 has more
            return find_k_smallest(nums2, j, nums1, i, k);
        }
        if (i == nums1.size()) { // nums1 is exhausted; take the kth number from nums2
            return nums2[j+k-1];
        }
        if (k == 1) { // Both arrays have available numbers; the minimum is the smaller of their first elements
            return min(nums1[i], nums2[j]);
        }
        // Try taking k/2 from nums1 and k-k/2 for j (so sj takes one extra when k is odd)
        int si = min(static_cast<int>(nums1.size()), i+k/2), sj = j + k - k/2;
        if (nums1[si-1] > nums2[sj-1]) { // Taking k/2 at i gives a value that is too large; j may need more and i fewer
            return find_k_smallest(nums1, i, nums2, sj, k - (sj - j));
        } else {
            // Taking k/2 at i gives a value that is too small; i may need more and j fewer
            return find_k_smallest(nums1, si, nums2, j, k - (si - i));
        }
    }
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int tot = nums1.size() + nums2.size();
        if (tot % 2 == 0) {
            // For an even count, average the tot/2-th and (tot/2+1)-th smallest numbers
            int left = find_k_smallest(nums1, 0, nums2, 0, tot/2);
            int right = find_k_smallest(nums1, 0, nums2, 0, tot/2+1);
            return (left+right)/2.0;
        }
        // For an odd count, the median is the (tot/2+1)-th smallest number
        return find_k_smallest(nums1, 0, nums2, 0, tot/2+1);
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
