# [Python] Memoized DFS: 100%

> Author: Benhao
> Date: 2021-05-29
> Upvotes: 9
> Tags: Python, Python3

---

### Approach
I did not see a memoized-search solution, so here is one. Pass a tuple instead of a list so that the arguments are hashable.

### Code

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
