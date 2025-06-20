import solution
from collections import deque
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestPathAllKeys(test_input)

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(grid), len(grid[0])
        goal = 0
        blocks = set()
        queue = deque()
        explored = set()
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '@':
                    queue.append((0, i, j))
                    explored.add((i, j, 0))
                elif 'a' <= cell <= 'f':
                    goal |= 1 << (ord(cell) - ord('a'))
                elif cell == '#':
                    blocks.add((i, j))

        steps = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                keys, x, y = queue.popleft()
                if keys == goal:
                    return steps
                for dx, dy in dirs:
                    if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n and (nx, ny) not in blocks:
                        c = grid[nx][ny]
                        if 'A' <= c <= 'F' and not (keys & (1 << (ord(c) - ord('A')))):
                            continue
                        new_keys = keys
                        if 'a' <= c <= 'f':
                            new_keys |= 1 << (ord(c) - ord('a'))
                            if new_keys == goal:
                                return steps + 1
                        if (nx, ny, new_keys) not in explored:
                            explored.add((nx, ny, new_keys))
                            queue.append((new_keys, nx, ny))
            steps += 1
        return -1