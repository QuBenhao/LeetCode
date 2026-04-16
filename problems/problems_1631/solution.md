# [Python] dijkstra

> Author: Benhao
> Date: 2022-06-04
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
按绝对之差最大值的最小依次dijkstra遍历

### 代码

```python3
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        pq = [(0, 0, 0)]
        explored = defaultdict(lambda:inf)
        explored[(0, 0)] = 0
        while pq:
            cost, x, y = heapq.heappop(pq)
            if x == m - 1 and y == n - 1:
                return cost
            for dx, dy in DIRS:
                if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n and explored[(nx, ny)] > max(cost, (d := abs(heights[nx][ny] - heights[x][y]))):
                    explored[(nx, ny)] = max(cost, d)
                    heapq.heappush(pq, (max(cost, d), nx, ny))
        return -1
```