import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDeletionSize(test_input)

    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        check_list = list(range(n - 1))

        ans = 0
        for j in range(m):
            for i in check_list:
                if strs[i][j] > strs[i + 1][j]:
                    # j 列不是升序，必须删
                    ans += 1
                    break
            else:
                # j 列是升序，不删更好
                new_size = 0
                for i in check_list:
                    if strs[i][j] == strs[i + 1][j]:
                        # 相邻字母相等，下一列 i 和 i+1 需要继续比大小
                        check_list[new_size] = i  # 原地覆盖
                        new_size += 1
                del check_list[new_size:]
        return ans
