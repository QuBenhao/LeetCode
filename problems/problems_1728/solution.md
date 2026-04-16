# [Python] 极小极大博弈

> Author: Benhao
> Date: 2022-05-09
> Upvotes: 25
> Tags: Python, Python3

---

### 解题思路

[和猫和老鼠一个思路](https://leetcode.cn/problems/cat-and-mouse/solution/pythonjavajavascriptgo-zui-da-zui-xiao-b-fyt8/)
实际状态最多有 8 * 8 * 8 * 8 * 2 种，可以用题目描述的1000作为界，但是Py会TLE。
猜测128为回合阈值，如果TLE可以调小一点，大于64，不会证明, 不保证正确性。

### 代码

```python3
DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        mm, nn = len(grid), len(grid[0])
        for x in range(mm):
            for y in range(nn):
                match grid[x][y]:
                    case 'C':
                        cat = x, y
                    case 'F':
                        food = x, y
                    case 'M':
                        mouse = x, y

        @lru_cache(None)
        def dfs(m, c, i):
            """
            极大极小博弈，
            老鼠尽量找自己获胜的，其次接受平局
            猫尽量找自己获胜的，其次接受平局

            :param m: 老鼠的位置
            :param c: 猫的位置
            :param i: 回合
            """
            if m == c or c == food or i > 128:
                return False
            if m == food:
                return True
            is_cat = False
            # 猫回合
            if i % 2:
                pos, jump = c, catJump
                is_cat = True
            else:
                pos, jump = m, mouseJump
            for dx, dy in DIRS:
                for jp in range(jump + 1):
                    nx, ny = pos[0] + dx * jp, pos[1] + dy * jp
                    if nx < 0 or ny < 0 or nx >= mm or ny >= nn or grid[nx][ny] == '#':
                        break
                    if not is_cat and dfs((nx, ny), c, i + 1):
                        return True
                    elif is_cat and not dfs(m, (nx, ny), i + 1):
                        return False
            return is_cat
        
        return dfs(mouse, cat, 0)

```
