import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMoves(*test_input)

    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if sx == tx and sy == ty:
            return 0
        if sx > tx or sy > ty:
            return -1
        if tx == ty:
            if sx == 0:
                sx, sy, tx, ty = sy, sx, ty, tx
            ans = self.minMoves(sx, sy, tx, 0)
        else:
            if tx < ty:
                sx, sy, tx, ty = sy, sx, ty, tx
            if tx > ty * 2:
                if tx % 2 != 0:
                    return -1
                ans = self.minMoves(sx, sy, tx // 2, ty)
            else:
                ans = self.minMoves(sx, sy, tx - ty, ty)
        return ans + 1 if ans != -1 else -1
