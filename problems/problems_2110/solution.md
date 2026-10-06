# [Python] Sliding with two pointers

> Author: Benhao
> Date: 2021-12-21
> Upvotes: 1
> Tags: Python, Python3

---

### Code

```python3
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        l = r = ans = 0
        while l < len(prices):
            while r < len(prices) - 1 and prices[r] - prices[r + 1] == 1:
                r += 1
            r += 1
            ans += (r - l + 1) * (r - l) // 2
            l = r
        return ans

```
