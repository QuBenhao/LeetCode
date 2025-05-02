from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pushDominoes(test_input)

    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        right = [inf] * n
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                right[i] = i
            elif dominoes[i] == '.':
                if i < n - 1 and right[i + 1] != inf:
                    right[i] = right[i + 1]
        prev = -inf
        ans = []
        for i, c in enumerate(dominoes):
            if c == 'R':
                ans.append('R')
                prev = i
            elif c == 'L':
                ans.append('L')
                prev = -inf
            else:
                left_dis, right_dis = i - prev, right[i] - i
                if left_dis > right_dis:
                    ans.append('L')
                elif left_dis < right_dis:
                    ans.append('R')
                else:
                    ans.append('.')
        return ''.join(ans)
