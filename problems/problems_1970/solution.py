import solution
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.latestDayToCross(*test_input)

    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        # Process forward, connecting left to right with eight-directional adjacency
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        # Water connected to the left boundary
        visited = set()
        # Water not yet connected to the left boundary
        wait = set()

        # Expand connected water with DFS over the surrounding 3x3 neighborhood
        def dfs(x, y):
            if y == col:
                return True
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (nx, ny) in wait:
                    wait.remove((nx, ny))
                    visited.add((nx, ny))
                    if dfs(nx, ny):
                        return True
            return False

        # Traverse cells in order
        for i, (x, y) in enumerate(cells):
            flag = False
            # Start from the left boundary
            if y == 1:
                flag = True
            # Away from the left boundary, check the surrounding 3x3 neighborhood for a connection
            else:
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in visited:
                        flag = True
                        break
            # If this water cell is connected, use DFS to connect water cells currently in wait
            if flag:
                visited.add((x, y))
                if dfs(x, y):
                    return i
            # Not yet connected; add to wait
            else:
                wait.add((x, y))
