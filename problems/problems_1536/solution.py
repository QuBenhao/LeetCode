import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSwaps(test_input)

    def minSwaps(self, grid: List[List[int]]) -> int:
        # 预处理每一行的尾零个数
        n = len(grid)
        tail_zeros = [n] * n
        for i in range(n):
            for j in range(n - 1, -1, -1):
                if grid[i][j]:
                    tail_zeros[i] = n - 1 - j
                    break

        ans = 0
        for i in range(n - 1):
            need_zeros = n - 1 - i
            for j in range(i, n):
                if tail_zeros[j] >= need_zeros:
                    ans += j - i
                    # 从 j 换到 i，原来 [i, j-1] 中的数据全体右移一位
                    tail_zeros[i + 1: j + 1] = tail_zeros[i: j]
                    break
            else:  # 没找到符合要求的 tail_zeros[j]
                return -1
        return ans
