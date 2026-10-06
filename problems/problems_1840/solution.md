# [Python] Reference implementation with my comments

> Author: Benhao
> Date: 2021-04-25
> Upvotes: 6
> Tags: Python

---

### Approach
During the contest, I realized the maximum middle height could be derived from both sides. I checked restrictions from left to right but missed the right-to-left pass.

### Code

```python3
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.extend([[1,0],[n,n-1]])
        restrictions.sort()
        m = len(restrictions)
        # The key is making every restriction valid and effective
        # Height limit at the right boundary
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0])
        # Height limit at the left boundary
        for i in range(1, m):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + restrictions[i][0] - restrictions[i-1][0])

        ans = 0
        for i in range(1, m):
            l, limit_l = restrictions[i-1]
            r, limit_r = restrictions[i]
            # Derive the maximum height from the left and right limits
            # We have h_max - limit_l <= max_idx - l and h_max - limit_r <= r - max_idx
            # Adding them gives h_max <= (r - l + limit_r + limit_l) // 2
            ans = max(ans, (r + limit_l + limit_r - l) // 2)
        return ans

```
