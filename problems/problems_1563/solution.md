# [Python] Optimized memoized search (DP) (100%)

> Author: Benhao
> Date: 2021-06-17
> Upvotes: 4
> Tags: Python, Python3

---

### Approach
The basic search does not use left_dfs or right_dfs, so each call must iterate to find the maximum.
```python3
            left = idx - 1
            right = idx
            if presum[idx] == half:
                ans = max(ans, presum[idx] - presum[i] + dfs(i, idx - 1), presum[idx] - presum[i] + dfs(idx, j))
                right += 1
            for k in range(i, left):
                ans = max(ans, presum[k + 1] - presum[i] + dfs(i, k))
            for k in range(right, j + 1):
                ans = max(ans, presum[j + 1] - presum[k] + dfs(k, j))
            return ans
```
When searches overlap, finding the maximum still requires comparing the same (i,k) or (k,j) intervals individually, repeating work.
If we cache the maximum for the left and right searches over an interval such as `(i,left)`, then searching `(i,left+1)` only requires comparing `presum[left+2]-presum[i] + dfs(i, left+1)` with the cached maximum for `(i,left)`.

Replace the loop that finds the maximum with memoized recursion to retain maxima for different intervals.

### Code

```python3
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            ans = 0
            half = (presum[j + 1] + presum[i]) / 2
            # Use binary search to find where the left and right sums balance
            idx = bisect.bisect_left(presum, half, lo=i, hi=j + 1)
            # Left of idx, left is smaller; right of idx, right is smaller
            if presum[idx] == half:
                ans = max(ans, left_dfs(i, idx), right_dfs(idx, j))
            else:
                ans = max(ans, left_dfs(i, idx-1))
                ans = max(ans, right_dfs(idx, j))
            return ans

        @lru_cache(None)
        def left_dfs(i, j):
            if i >= j:
                return 0
            return max(presum[j] - presum[i] + dfs(i, j-1), left_dfs(i, j-1))

        @lru_cache(None)
        def right_dfs(i, j):
            if i >= j+1:
                return 0
            return max(presum[j+1] - presum[i] + dfs(i, j), right_dfs(i+1, j))

        presum = [0] + list(accumulate(stoneValue))
        return dfs(0, len(stoneValue) - 1)
```
