import solution
from collections import deque
from typing import List


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hasValidPath([x[:] for x in test_input])

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # Directions: up (0), right (1), down (2), left (3)
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        # Directions connected by each street type
        street_dirs = {
            1: {1, 3},    # Left, right
            2: {0, 2},    # Up, down
            3: {2, 3},    # Down, left
            4: {1, 2},    # Right, down
            5: {0, 3},    # Up, left
            6: {0, 1},    # Up, right
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
                # Check whether the neighboring cell allows entry from the opposite direction
                nd = (d + 2) % 4  # Opposite direction
                if nd in street_dirs[grid[nx][ny]]:
                    if nx == m - 1 and ny == n - 1:
                        return True
                    visited.add((nx, ny))
                    q.append((nx, ny))
        return False
