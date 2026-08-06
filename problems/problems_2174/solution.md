# [Python] 状压dp

> slug: python-zhuangya-by-himymben-wvn9
> date: 2022-04-25
> tags: Python, Python3
> question: Remove All Ones With Row and Column Flips II (remove-all-ones-with-row-and-column-flips-ii)
> url: https://leetcode.cn/problems/remove-all-ones-with-row-and-column-flips-ii/solutions/7lk311/python-zhuangya-by-himymben-wvn9/

---
### 解题思路
用二进制 1 << (i * n + j) 位表示grid[i][j]是否为1的状压
使用了记忆化递归写dp

### 代码

```python3
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(state):
            if not state:
                return 0
            ans = inf
            for i in range(m * n):
                if (1 << i) & state:
                    row, col = divmod(i, n)
                    nxt_state = state
                    for r in range(m):
                        if (b:= 1 << (r * n + col)) & nxt_state:
                            nxt_state ^= b
                    for c in range(n):
                        if (b:= 1 << (row * n + c)) & nxt_state:
                            nxt_state ^= b
                    ans = min(ans, dfs(nxt_state))
            return ans + 1
        
        return dfs(sum(1 << (i * n + j) if grid[i][j] else 0 for i in range(m) for j in range(n)))
```