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
        # 正序，从左至右，八连通
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        # 最左侧出发可连通水域
        visited = set()
        # 最左侧出发暂未连通水域
        wait = set()

        # 增加连通水域，根据九宫格dfs
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

        # 依此遍历cells
        for i, (x, y) in enumerate(cells):
            flag = False
            # 最左侧出发
            if y == 1:
                flag = True
            # 非最左侧，根据九宫格判断能否连通
            else:
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in visited:
                        flag = True
                        break
            # 若当前水域可连通，则通过dfs尝试取出wait内的水域
            if flag:
                visited.add((x, y))
                if dfs(x, y):
                    return i
            # 暂未连通，丢入wait
            else:
                wait.add((x, y))
