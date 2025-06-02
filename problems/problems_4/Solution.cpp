//go:build ignore
#include "cpp/common/Solution.h"

using namespace std;
using json = nlohmann::json;

class Solution {
    int find_k_smallest(vector<int>& nums1, int i, vector<int>& nums2, int j, int k) {
        // 从两个有序数组中找到第k小的数
        if (nums1.size() - i > nums2.size() - j) { // 交换, 确保nums1中可选数更少, nums2中更多
            return find_k_smallest(nums2, j, nums1, i, k);
        }
        if (i == nums1.size()) { // nums1中已选完, 从nums2里拿第k个
            return nums2[j+k-1];
        }
        if (k == 1) { // nums1和nums2都有可选的数, 最小值数两者首个元素中更小的那个
            return min(nums1[i], nums2[j]);
        }
        // 尝试从nums1中取k/2个, j里面直接取k-k/2 (确保k是奇数时sj多取一个)
        int si = min(static_cast<int>(nums1.size()), i+k/2), sj = j + k - k/2;
        if (nums1[si-1] > nums2[sj-1]) { // i取k/2的偏大了，说明j可能能取更多,i可能要取更少
            return find_k_smallest(nums1, i, nums2, sj, k - (sj - j));
        } else {
            // i取k/2的偏小了，说明i可能要取更多, j可能要取更少
            return find_k_smallest(nums1, si, nums2, j, k - (si - i));
        }
    }
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int tot = nums1.size() + nums2.size();
        if (tot % 2 == 0) {
            // 偶数个，中位数要找第tot/2个小的和第tot/2+1个小的的平均值
            int left = find_k_smallest(nums1, 0, nums2, 0, tot/2);
            int right = find_k_smallest(nums1, 0, nums2, 0, tot/2+1);
            return (left+right)/2.0;
        }
        // 奇数个, 中位数就是tot/2+1小
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
