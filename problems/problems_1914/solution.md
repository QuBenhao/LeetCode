# [Python] 逐层旋转

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
每层旋转的循环是根据该层的元素个数的 (k%len),旋转len次不变

### 代码

```python3
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def nums(x, y, lm, ln):
            ans = []
            for j in range(y, y + ln):
                ans.append(grid[x][j])
            for i in range(x + 1, x + lm):
                ans.append(grid[i][y + ln - 1])
            for j in range(y + ln - 2, y - 1, -1):
                ans.append(grid[x + lm - 1][j])
            for i in range(x + lm - 2, x, -1):
                ans.append(grid[i][y])
            return ans

        # 当前层的长宽
        m, n = len(grid), len(grid[0])
        # 当前层的左上角坐标
        x = y = 0
        d = dict()
        while m and n:
            # 该层的所有元素
            val = nums(x, y, m, n)
            temp = k % len(val)
            # 该层旋转后的顺序
            val = val[temp:] + val[:temp]
            idx = 0
            for j in range(y, y + n):
                grid[x][j] = val[idx]
                idx += 1
            for i in range(x + 1, x + m):
                grid[i][y + n - 1] = val[idx]
                idx += 1
            for j in range(y + n - 2, y - 1, -1):
                grid[x + m - 1][j] = val[idx]
                idx += 1
            for i in range(x + m - 2, x, -1):
                grid[i][y] = val[idx]
                idx += 1
            x += 1
            y += 1
            m -= 2
            n -= 2
        return grid
```