# [Python] 记忆化dfs 100%

> Author: Benhao
> Date: 2021-05-29
> Upvotes: 9
> Tags: Python, Python3

---

### 解题思路
看了一圈没有发记忆化搜索的，那写一个吧。传参用tuple而不是list，这样才有hash值。

### 代码

```python3
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, vals):
            if idx == len(nums1) - 1:
                return nums1[idx] ^ vals[0]
            ans = float("inf")
            for val in vals:
                tp = list(vals)
                tp.remove(val)
                ans = min(ans, dfs(idx+1,tuple(tp)) + (nums1[idx] ^ val))
            return ans
        return dfs(0, tuple(sorted(nums2)))
```