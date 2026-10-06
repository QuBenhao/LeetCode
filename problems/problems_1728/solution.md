# [Python] Minimax game

> Author: Benhao
> Date: 2022-05-09
> Upvotes: 25
> Tags: Python, Python3

---

### Approach

[The same idea as Cat and Mouse](https://leetcode.cn/problems/cat-and-mouse/solution/pythonjavajavascriptgo-zui-da-zui-xiao-b-fyt8/)
There are at most 8 * 8 * 8 * 8 * 2 states. The statement's limit of 1000 turns can be used, but Python times out.
I guessed a threshold of 128 turns; if it times out, try a smaller value above 64. I do not have a proof and cannot guarantee correctness.

### Code

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
            Minimax game:
            The mouse prefers a win, then a draw
            The cat prefers a win, then a draw

            :param m: Mouse position
            :param c: Cat position
            :param i: Turn
            """
            if m == c or c == food or i > 128:
                return False
            if m == food:
                return True
            is_cat = False
            # Cat's turn
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
