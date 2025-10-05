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
                    row[j] = -1  # 标记 (i,j) 访问过
        heapify(h)

        ans = 0
        while h:
            min_height, i, j = heappop(h)  # min_height 是木桶的短板
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < m and 0 <= y < n and heightMap[x][y] >= 0:  # (x,y) 没有访问过
                    # 如果 (x,y) 的高度小于 min_height，那么接水量为 min_height - heightMap[x][y]
                    ans += max(min_height - heightMap[x][y], 0)
                    # 给木桶新增一块高为 max(min_height, heightMap[x][y]) 的木板
                    heappush(h, (max(min_height, heightMap[x][y]), x, y))
                    heightMap[x][y] = -1  # 标记 (x,y) 访问过
        return ans
