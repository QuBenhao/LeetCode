# [Python] Dynamic programming (backward) or memoized search (forward)

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
1. Removing stones and putting their sum back **does not change the prefix sums**.
2. The maximum gain from i depends on the maximum gain from a position j to its right, which is why the recurrence runs backward.
This works because:
```
dp[i] = max(presum[j] - dp[j] for j in range(i+1, n-1))
```
The backward recurrence can be reduced to one dimension:
Taking `presum-res` means stopping at the optimal j; taking `res` means skipping that stopping point and retaining the best value available from j.
```
res = max(res, presum - res)
```
Here, presum corresponds to the j associated with res.

Based on [this solution](https://leetcode.com/problems/stone-game-viii/discuss/1224639/Python-prefix-sum)

### Code

```python3
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # 1. Remove the leftmost x stones and put their sum on the left; presum[x] remains unchanged
        # 2. The maximum gain at i is the largest presum[j] - dp[j] over j to its right
        for i in range(1, len(stones)):
            stones[i] += stones[i-1]

        res = stones[-1]
        for num in stones[-2:0:-1]:
            # Stop at j to gain presum[j], while the opponent can gain at most dp[j]
            # Or skip j and retain the score dp[j]
            res = max(num - res, res)
        return res

```
Direct search with memoized range maxima just manages to pass.
```python3
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Removing and replacing leaves prefix sums unchanged
        # Each move includes the preceding prefix sum
        @lru_cache(None)
        def dfs(idx):
            if idx >= n - 1:
                return presum[n]
            # Skipping this index gives dfs(idx+1); choosing it gives presum[idx+1] - dfs(idx+1). Take the maximum
            return max(dfs(idx + 1), presum[idx + 1] - dfs(idx+1))

        n = len(stones)
        presum = [0] + list(accumulate(stones))
        dfs.cache_clear()
        return dfs(1)
```
