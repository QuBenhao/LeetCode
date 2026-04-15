# [Python] 双指针

> Author: Benhao
> Date: 2021-05-09
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
利用两个数组非递增的性质

### 代码

```python3
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        i = j = 0
        ans = 0
        while j < n:
            # 如果nums1[i]是大于当前的nums2[j]的，i需要右移
            # i不该超过j，否则不满足i<=j
            while i < min(m, j) and nums1[i] > nums2[j]:
                i += 1
            if i == m:
                return ans
            # 对于当前j最远的满足nums1[i]<=nums2[j]就是i了
            ans = max(ans, j - i)
            j += 1
        return ans

```