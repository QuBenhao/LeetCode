from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pyramidTransition(*test_input)

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # n = len(bottom)
        # final_pyramid = [[''] * i for i in range(1, n)]
        # final_pyramid.append(list(bottom))
        # allowed_map = defaultdict(list)
        # for allow in allowed:
        #     allowed_map[allow[:2]].append(allow[2])
        #
        # def dfs(i, j):
        #     if i == 0:
        #         return True
        #     if j == i:
        #         return dfs(i - 1, 0)
        #
        #     k = final_pyramid[i][j] + final_pyramid[i][j + 1]
        #     for available in allowed_map[k]:
        #         final_pyramid[i - 1][j] = available
        #         if dfs(i, j + 1):
        #             return True
        #     final_pyramid[i - 1][j] = ''
        #     return False
        #
        # return dfs(n - 1, 0)

        groups = [[[] for _ in range(7)] for _ in range(7)]
        for a, b, c in allowed:
            groups[ord(a) & 31][ord(b) & 31].append(ord(c) & 31)

        n = len(bottom)
        pyramid = [0] * n
        for i, ch in enumerate(bottom):
            pyramid[-1] |= (ord(ch) & 31) << (i * 3)

        vis = set()
        def dfs(i, j):
            if i < 0:
                return True
            if pyramid[i] in vis:
                return False
            if j == i + 1:
                vis.add(pyramid[i])
                return dfs(i - 1, 0)

            # 7 represents the lowest three bits; convert them to a three-character string
            for t in groups[pyramid[i + 1] >> (j * 3) & 7][pyramid[i + 1] >> ((j + 1) * 3) & 7]:
                pyramid[i] &= ~(7 << (j * 3)) # Clear first
                pyramid[i] |= t << (j * 3) # Fill in top
                if dfs(i, j + 1):
                    return True

            return False

        return dfs(n - 2, 0)
