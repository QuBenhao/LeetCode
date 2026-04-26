import solution
from collections import deque
from typing import List


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hasValidPath([x[:] for x in test_input])

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # 方向: 上(0), 右(1), 下(2), 左(3)
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        # 每条街道可以通往的方向
        street_dirs = {
            1: {1, 3},    # 左、右
            2: {0, 2},    # 上、下
            3: {2, 3},    # 下、左
            4: {1, 2},    # 右、下
            5: {0, 3},    # 上、左
            6: {0, 1},    # 上、右
        }

        m, n = len(grid), len(grid[0])
        if m == n == 1:
            return True

        q = deque([(0, 0)])
        visited = {(0, 0)}

        while q:
            x, y = q.popleft()
            street = grid[x][y]
            for d in street_dirs[street]:
                nx, ny = x + dx[d], y + dy[d]
                if not (0 <= nx < m and 0 <= ny < n):
                    continue
                if (nx, ny) in visited:
                    continue
                # 检查相邻格子能否从相反方向进入
                nd = (d + 2) % 4  # 相反方向
                if nd in street_dirs[grid[nx][ny]]:
                    if nx == m - 1 and ny == n - 1:
                        return True
                    visited.add((nx, ny))
                    q.append((nx, ny))
        return False
