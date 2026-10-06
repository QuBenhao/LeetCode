# [Python] Memoized DFS

> Author: Benhao
> Date: 2021-05-30
> Upvotes: 6
> Tags: Python, Python3

---

### Approach
Traverse cell by cell, following [memoized search in Java](https://leetcode.cn/problems/maximize-grid-happiness/solution/dong-tai-gui-hua-shi-jian-qia-de-you-dian-er-jin-y/).

For each cell, choose between leaving it empty, placing an introvert, or placing an extrovert.
The state need not store all m*n cells. When filling left to right and top to bottom, **only the upper and left neighbors may already be occupied**; the span from the upper neighbor to the left neighbor fits within `n columns`.
Keeping the last `n` cells is therefore enough to compute the change in happiness.

Use `0` for empty, `1` for an introvert, and `2` for an extrovert.
When computing happiness, remember that cells on the left boundary have no left neighbor.

### Code

```python3
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        @lru_cache(None)
        def dfs(x, y, intro, extro, state):
            if y == n:
                return dfs(x+1,0, intro, extro, state)
            if x == m:
                return 0
            # Keep the last n placements; earlier cells cannot be affected by this one
            l = list(state)
            # The upper neighbor is l[0], and the left neighbor is l[-1]

            # Leave the cell empty
            ans = dfs(x,y+1,intro,extro, tuple(l[1:] + [0]))

            # Place an introvert
            if intro:
                diff = 120
                if l[0] == 1:
                    diff -= 30 * 2
                elif l[0] == 2:
                    # One introvert and one extrovert
                    diff -= 10
                if y:
                    if l[-1] == 1:
                        diff -= 30 * 2
                    elif l[-1] == 2:
                        diff -= 10
                ans = max(ans, dfs(x,y+1, intro-1, extro, tuple(l[1:] + [1])) + diff)
            
            # Place an extrovert
            if extro:
                diff = 40
                if l[0] == 1:
                    diff -= 10
                elif l[0] == 2:
                    diff += 40
                if y:
                    if l[-1] == 1:
                        diff -= 10
                    elif l[-1] == 2:
                        diff += 40
                ans = max(ans, dfs(x,y+1, intro, extro - 1, tuple(l[1:] + [2])) + diff)
            return ans
        
        return dfs(0, 0, introvertsCount, extrovertsCount, tuple([0] * n))
```
