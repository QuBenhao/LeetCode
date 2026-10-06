import solution
from typing import *
from collections import deque
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumSafenessFactor(test_input)

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        Max heap (Dijkstra-style approach)

        Approach:
        1. Preprocess with multi-source BFS to find each cell's distance to the nearest thief
        2. Use a max-heap priority queue to expand the cell with the greatest safeness factor
        3. The safeness factor upon reaching the destination is the answer
        """
        n = len(grid)

        # Multi-source BFS: find each cell's distance to the nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        # Start from all thief positions
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        # Expand with BFS
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # Max heap: prioritize cells with the greatest safeness factor
        # Use negative values to simulate a max heap (Python's heapq is a min heap)
        heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while heap:
            safety, x, y = heapq.heappop(heap)
            safety = -safety  # Convert back to a positive value

            # Destination reached: return the current safeness factor
            if x == n - 1 and y == n - 1:
                return safety

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # The safeness factor is the minimum along the path
                    heapq.heappush(heap, (-min(safety, dist[nx][ny]), nx, ny))

        return 0

    # ==================== Binary-search solution (less efficient) ====================
    #
    # def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
    #     """
    #     Binary search on the answer + BFS feasibility check
    #
    #     Approach:
    #     1. Preprocess with multi-source BFS to find each cell's distance to the nearest thief
    #     2. Binary-search the safeness factor mid
    #     3. Use BFS to check for a path whose cells all have dist >= mid
    #     """
    #     n = len(grid)
    #
    #     # Multi-source BFS: find each cell's distance to the nearest thief
    #     dist = [[-1] * n for _ in range(n)]
    #     q = deque()
    #
    #     # Start from all thief positions
    #     for i in range(n):
    #         for j in range(n):
    #             if grid[i][j] == 1:
    #                 dist[i][j] = 0
    #                 q.append((i, j))
    #
    #     # Expand with BFS
    #     dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #     while q:
    #         x, y = q.popleft()
    #         for dx, dy in dirs:
    #             nx, ny = x + dx, y + dy
    #             if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
    #                 dist[nx][ny] = dist[x][y] + 1
    #                 q.append((nx, ny))
    #
    #     # Binary-search the answer
    #     def check(safety: int) -> bool:
    #         """Check whether a path with safeness factor >= safety exists"""
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
    #     # Binary-search range: [0, n] (the maximum distance does not exceed n)
    #     left, right = 0, n
    #     while left < right:
    #         mid = (left + right + 1) // 2
    #         if check(mid):
    #             left = mid
    #         else:
    #             right = mid - 1
    #
    #     return left

