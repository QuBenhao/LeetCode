# [Python] Memoized search accelerated by prefix sums

> Author: Benhao
> Date: 2021-06-16
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
We want the maximum number of stones the first player can take, while the second player tries to minimize that number.
On the first player's turn, use prefix sums to calculate the stones taken in the current move and add the number obtained recursively.

A common way to alternate turns in a minimax game is to use subtraction (Alice's stones are positive and Bob's are negative).

### Code

```python3
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, curr, p):
            if idx == n:
                return 0
            # One player can take all remaining stones
            if n - idx <= 2 * curr:
                return presum[-1] - presum[idx] if p else 0
            # Alice chooses the move with the largest eventual result
            if p:
                return max(dfs(idx + i, max(curr, i), not p) + presum[idx + i]
                           for i in range(1,2 * curr + 1)) - presum[idx]
            # Bob chooses the move that minimizes Alice's total
            return min(dfs(idx + i, max(curr, i), not p) for i in range(1, 2 * curr + 1))

        n = len(piles)
        presum = list(accumulate([0] + piles))
        return dfs(0, 1, True)
```
Use a minus sign instead of alternating p
```python3
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == n:
                return 0
            # One player can take all remaining stones
            if n - idx <= 2 * curr:
                return presum[-1] - presum[idx]
            # The maximum available now is the remaining total minus the smallest total we can leave the opponent
            return presum[-1] - presum[idx] - min(dfs(idx + i, max(i, curr)) for i in range(1, 2 * curr + 1))

        n = len(piles)
        presum = list(accumulate([0] + piles))
        return dfs(0, 1)
```
