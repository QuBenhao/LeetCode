import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.escapeMaze([x[:] for x in test_input])

    def escapeMaze(self, maze):
        """
        :type maze: List[List[str]]
        :rtype: bool
        """
        # Maze rows, columns, and the maximum time available to reach the destination
        m, n, t = len(maze[0]), len(maze[0][0]), len(maze)
        # Possible moves
        dir = [(-1, 0), (0, 0), (1, 0), (0, 1), (0, -1)]

        @ lru_cache(None)
        def dfs(x, y, time, magicA, magicB):
            if x == m - 1 and y == n - 1:
                return True
            if time + 1 == t or t - time - 1 < m - x + n - y - 2:
                return False

            for dx,dy in dir:
                x_, y_ = x + dx, y + dy
                if x_ < 0 or x_ == m or y_ < 0 or y_ == n:
                    continue
                # This location is traversable at the next time step
                if maze[time+1][x_][y_] == '.':
                    if dfs(x_, y_, time+1, magicA, magicB):
                        return True
                # A scroll is needed at the next time step
                else:
                    # Use the temporary scroll
                    if magicA:
                        if dfs(x_, y_, time+1, False, magicB):
                            return True
                    # Use the permanent scroll
                    if magicB:
                        # A permanent scroll lets us stay here indefinitely (equivalently, leave and return at the next time step)
                        for next_time in range(time+1, t):
                            if dfs(x_, y_, next_time, magicA, False):
                                return True
            return False

        return dfs(0, 0, 0, True, True)
