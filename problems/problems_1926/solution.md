# [Python] BFS

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
很标准的BFS板子

### 代码

```python3
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        entrance = (entrance[0], entrance[1])
        m, n = len(maze), len(maze[0])
        q = deque([(entrance, 0)])
        explored = {entrance}
        while q:
            pos, step = q.popleft()
            if pos != entrance and (pos[0] == 0 or pos[0] == m - 1 or pos[1] == 0 or pos[1] == n - 1):
                return step
            x, y = pos
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                if 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == '.' and (
                x + dx, y + dy) not in explored:
                    explored.add((x + dx, y + dy))
                    q.append(((x + dx, y + dy), step + 1))
        return -1

```