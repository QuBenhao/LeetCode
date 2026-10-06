# [Python] Depth-first search

> slug: python-shen-du-you-xian-sou-suo-by-himym-ihx2
> date: 2022-05-02
> tags: Python, Python3
> question: Number of Spaces Cleaning Robot Cleaned (number-of-spaces-cleaning-robot-cleaned)
> url: https://leetcode.cn/problems/number-of-spaces-cleaning-robot-cleaned/solutions/1mDY7i/python-shen-du-you-xian-sou-suo-by-himym-ihx2/

---
### Approach
Simulate the robot moving forward. Mark each position and direction pair to detect previously visited states.

### Code

```python3
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        m, n, ans, explored = len(room), len(room[0]), set(), set()
        def dfs(x, y, idx):
            if (x, y, idx) in explored:
                return
            ans.add((x, y))
            explored.add((x, y, idx))
            if 0 <= (nx := x + DIRS[idx][0]) < m and 0 <= (ny := y + DIRS[idx][1]) < n and not room[nx][ny]:
                dfs(nx, ny, idx)
            else:
                dfs(x, y, (idx + 1) % 4)
 
        dfs(0, 0, 0)
        return len(ans)
```
