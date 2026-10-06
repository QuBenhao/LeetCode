# [Python] Enumerate the two players' positions in the next round

> Author: Benhao
> Date: 2021-06-14
> Upvotes: 5
> Tags: Python, Python3

---

### Approach
Based on [this code](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/discuss/1268452/Python-2-Solution%3A-dfs-and-smart-dp-explained)

### Code

```python3
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dp(l, r, m):
            if l > r:
                return dp(r, l, m)
            # The two players reach the same position, meaning they compete
            if l == r:
                return 1, 1

            earliest, latest = inf, 0
            # Next l ranges from 1 (everyone before l loses) to l (everyone before l wins)
            for i in range(1, l + 1):
                # Next r ranges from l-i+1 (everyone between r and l loses) to r-i (everyone between them wins)
                for j in range(l - i + 1, r - i + 1):
                    if not (m + 1) // 2 >= i + j >= l + r - m // 2:
                        continue
                    ea, la = dp(i, j, (m + 1) // 2)
                    earliest = min(earliest, ea + 1)
                    latest = max(latest, la + 1)
            return earliest, latest

        return list(dp(firstPlayer, n - secondPlayer + 1, n))
```
