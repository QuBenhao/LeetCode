import solution
from typing import *
from collections import deque
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumSafenessFactor(test_input)

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        最大堆 (Dijkstra 思想)

        思路：
        1. 多源 BFS 预处理：计算每个格子到最近小偷的距离
        2. 用最大堆优先队列，每次选择安全系数最大的格子扩展
        3. 到达终点时的安全系数即为答案
        """
        n = len(grid)

        # 多源 BFS：计算每个格子到最近小偷的距离
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # 将所有小偷位置作为起点
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        # BFS 扩展
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # 最大堆：优先走安全系数最大的格子
        # 用负数模拟最大堆 (Python heapq 是最小堆)
        heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while heap:
            safety, x, y = heapq.heappop(heap)
            safety = -safety  # 转回正数

            # 到达终点，返回当前安全系数
            if x == n - 1 and y == n - 1:
                return safety

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # 安全系数取路径上的最小值
                    heapq.heappush(heap, (-min(safety, dist[nx][ny]), nx, ny))

        return 0

    # ==================== 二分答案解法（效率较低） ====================
    #
    # def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
    #     """
    #     二分答案 + BFS 可行性检查
    #
    #     思路：
    #     1. 多源 BFS 预处理：计算每个格子到最近小偷的距离
    #     2. 二分安全系数 mid
    #     3. BFS 检查是否存在路径，使得路径上所有格子 dist >= mid
    #     """
    #     n = len(grid)
    #
    #     # 多源 BFS：计算每个格子到最近小偷的距离
    #     dist = [[-1] * n for _ in range(n)]
    #     q = deque()
    #
    #     # 将所有小偷位置作为起点
    #     for i in range(n):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 dist[i][j] = 0
    #                 q.append((i, j))
    #
    #     # BFS 扩展
    #     dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #     while q:
    #         x, y = q.popleft()
    #         for dx, dy in dirs:
    #             nx, ny = x + dx, y + dy
    #             if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
    #                 dist[nx][ny] = dist[x][y] + 1
    #                 q.append((nx, ny))
    #
    #     # 二分答案
    #     def check(safety: int) -> bool:
    #         """检查是否存在安全系数 >= safety 的路径"""
    #         if dist[0][0] < safety:
    #             return False
    #         visited = [[False] * n for _ in range(n)]
    #         q = deque([(0, 0)])
    #         visited[0][0] = True
    #         while q:
    #             x, y = q.popleft()
    #             if x == n - 1 and y == n - 1:
    #                 return True
    #             for dx, dy in dirs:
    #                 nx, ny = x + dx, y + dy
    #                 if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and dist[nx][ny] >= safety:
    #                     visited[nx][ny] = True
    #                     q.append((nx, ny))
    #         return False
    #
    #     # 二分范围：[0, n] (最大距离不会超过 n)
    #     left, right = 0, n
    #     while left < right:
    #         mid = (left + right + 1) // 2
    #         if check(mid):
    #             left = mid
    #         else:
    #             right = mid - 1
    #
    #     return left

