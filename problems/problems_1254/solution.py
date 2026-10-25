import sys

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.closedIsland(test_input)

    def closedIsland(self, grid: list[list[int]]) -> int:
        # 0 is land, 1 is water. A closed island is a land component that
        # never reaches the grid border.
        UNVISITED, IN_PROGRESS, DONE = 0, 1, 2
        m, n = len(grid), len(grid[0])
        state = [[UNVISITED] * n for _ in range(m)]
        sys.setrecursionlimit(max(10000, m * n + 1000))

        def dfs(i: int, j: int) -> bool:
            if not (0 <= i < m and 0 <= j < n):
                return False  # left the grid: this island touches the border
            if grid[i][j] == 1 or state[i][j] == DONE:
                return True  # water / finished: identity of AND
            if state[i][j] == IN_PROGRESS:
                return True  # on the stack: still unknown, contributes identity
            state[i][j] = IN_PROGRESS
            ok = True
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                # no short-circuit: the whole island must be marked DONE
                ok &= dfs(i + di, j + dj)
            state[i][j] = DONE
            return ok

        return sum(
            dfs(i, j)
            for i in range(m)
            for j in range(n)
            if grid[i][j] == 0 and state[i][j] == UNVISITED
        )
