# [Python] Prefix sums + memoized recursion

> Author: Benhao
> Date: 2022-03-27
> Upvotes: 11
> Tags: Python, Python3

---

### Approach
In other words, this is a brute-force approach that considers the best value obtainable from each stack.

dfs(idx, r) is the maximum value obtainable starting at piles[idx] with r picks remaining.
If we take $x$ coins from piles[idx], the result is the best value obtainable afterward plus the current sum: dfs(idx + 1, r - x) + sum(piles[idx][:x]). [Use prefix sums here to avoid repeated calculation.]
Take the maximum over these choices.

### Code

```python3
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        presums, n = [[0] + list(accumulate(p)) for p in piles], len(piles)
        
        @lru_cache(None)
        def dfs(idx, r):
            return max(dfs(idx + 1, r - i) + presums[idx][i] for i in range(min(r, len(piles[idx])) + 1)) if idx < n and r else 0
        
        return dfs(0, k)
```
