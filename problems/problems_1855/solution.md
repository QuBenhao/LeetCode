# [Python] Two pointers

> Author: Benhao
> Date: 2021-05-09
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
Use the fact that both arrays are nonincreasing.

### Code

```python3
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        i = j = 0
        ans = 0
        while j < n:
            # If nums1[i] exceeds nums2[j], move i right
            # i must not pass j, since i<=j is required
            while i < min(m, j) and nums1[i] > nums2[j]:
                i += 1
            if i == m:
                return ans
            # This i is the farthest from j that satisfies nums1[i]<=nums2[j]
            ans = max(ans, j - i)
            j += 1
        return ans

```
