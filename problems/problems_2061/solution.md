# [Python] 深度优先搜索

> slug: python-shen-du-you-xian-sou-suo-by-himym-ihx2
> date: 2022-05-02
> tags: Python, Python3
> question: Number of Spaces Cleaning Robot Cleaned (number-of-spaces-cleaning-robot-cleaned)
> url: https://leetcode.cn/problems/number-of-spaces-cleaning-robot-cleaned/solutions/1mDY7i/python-shen-du-you-xian-sou-suo-by-himym-ihx2/

---
### 解题思路
模拟机器人一直往前走就行了。标记位置+方向作为走过的判断

### 代码

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