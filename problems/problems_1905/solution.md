# [Python] DFS over connected components in grid 2

> Author: Benhao
> Date: 2021-06-20
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
If a cell is 1 in grid 2 but 0 in grid 1, its island cannot be a sub-island.

### Code

```python3
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        explored = set()
        m, n = len(grid1), len(grid1[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i == m or j == n:
                return -1
            if not grid2[i][j] or (i,j) in explored:
                return -1
            if not grid1[i][j]:
                return 0
            explored.add((i,j))

            mark = 1
            for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
                q = dfs(i+dx,j+dy)
                if q == 0:
                    mark = 0
            return mark
        
        ans = 0
    
        for i in range(m):
            for j in range(n):
                if grid2[i][j] and (i,j) not in explored:
                    if dfs(i,j) == 1:
                        ans += 1
        return ans
```
