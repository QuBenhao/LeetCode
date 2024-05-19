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
        # 迷宫的行数、列数以及到达终点最多的时间
        m, n, t = len(maze[0]), len(maze[0][0]), len(maze)
        # 移动方式
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
                # 下一个时刻该地点可以走
                if maze[time+1][x_][y_] == '.':
                    if dfs(x_, y_, time+1, magicA, magicB):
                        return True
                # 下一个时刻需要使用卷轴
                else:
                    # 使用临时卷轴
                    if magicA:
                        if dfs(x_, y_, time+1, False, magicB):
                            return True
                    # 使用永久卷轴
                    if magicB:
                        # 使用永久卷轴的意义相当于在原地停留无限长的时间 （等价于离开这里再在下一个时刻回到这里）
                        for next_time in range(time+1, t):
                            if dfs(x_, y_, next_time, magicA, False):
                                return True
            return False

        return dfs(0, 0, 0, True, True)
