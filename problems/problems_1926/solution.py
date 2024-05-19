import solution
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nearestExit(*test_input)

    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        entrance = (entrance[0], entrance[1])
        m, n = len(maze), len(maze[0])
        q = deque([(entrance, 0)])
        explored = {entrance}
        while q:
            pos, step = q.popleft()
            if pos != entrance and (pos[0] == 0 or pos[0] == m - 1 or pos[1] == 0 or pos[1] == n - 1):
                return step
            x, y = pos
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                if 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == '.' and (x + dx, y + dy) not in explored:
                    explored.add((x + dx, y + dy))
                    q.append(((x + dx, y + dy), step + 1))
        return -1
