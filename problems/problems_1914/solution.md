# [Python] 逐层旋转 - 方向数组法

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路

矩阵由多层同心方环组成，每层独立旋转。逆时针旋转 `k` 次，等价于将元素数组左移 `k % len` 位。

**优化思路**：用**方向数组**统一生成坐标，避免4个独立循环。

方向数组 `dirs = [(0,1), (1,0), (0,-1), (-1,0)]` 分别对应右、下、左、上四个方向，配合各边长度循环，一气呵成生成所有坐标。这种模式在网格题（DFS/BFS/螺旋矩阵）中都能复用。

### 代码

```python3 []
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # 方向：右、下、左、上（逆时针）
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for layer in range(min(m, n) // 2):
            top, left = layer, layer
            bottom, right = m - 1 - layer, n - 1 - layer
            # 各边长度
            lengths = [right - left, bottom - top, right - left, bottom - top]

            # 生成该层坐标（逆时针顺序）
            coords = []
            i, j = top, left
            for (di, dj), length in zip(dirs, lengths):
                for _ in range(length):
                    coords.append((i, j))
                    i += di
                    j += dj

            # 提取、旋转、写回
            vals = [grid[r][c] for r, c in coords]
            shift = k % len(vals)
            vals = vals[shift:] + vals[:shift]

            for (r, c), v in zip(coords, vals):
                grid[r][c] = v

        return grid
```
