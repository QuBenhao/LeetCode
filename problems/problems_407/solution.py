import solution
from typing import *
from heapq import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.trapRainWater(test_input)

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        h = []
        for i, row in enumerate(heightMap):
            for j, height in enumerate(row):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    h.append((height, i, j))
                    row[j] = -1  # Mark (i,j) as visited
        heapify(h)

        ans = 0
        while h:
            min_height, i, j = heappop(h)  # min_height is the lowest boundary of the container
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < m and 0 <= y < n and heightMap[x][y] >= 0:  # (x,y) has not been visited
                    # If (x,y) is lower than min_height, it holds min_height - heightMap[x][y] water
                    ans += max(min_height - heightMap[x][y], 0)
                    # Extend the container with a boundary of height max(min_height, heightMap[x][y])
                    heappush(h, (max(min_height, heightMap[x][y]), x, y))
                    heightMap[x][y] = -1  # Mark (x,y) as visited
        return ans
