import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.fallingSquares(test_input)

    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        pos = set()
        for a, length in positions:
            pos.add(a)
            pos.add(a + length - 1)
        idx_map = {v: i for i, v in enumerate(sorted(pos))}
        records = [0] * len(idx_map)
        ans, cur = [], 0
        for a, length in positions:
            left, right = idx_map[a], idx_map[a + length - 1]
            new_height = max(records[left:right + 1]) + length
            for i in range(left, right + 1):
                records[i] = new_height
            cur = max(cur, new_height)
            ans.append(cur)
        return ans
