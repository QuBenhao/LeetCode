from math import log10

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lexicalOrder(test_input)

    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        j = 1
        for i in range(n):
            ans.append(j)
            if j * 10 <= n: # 能乘10的时候优先乘10
                j *= 10
            else:
                while j % 10 == 9 or j + 1 > n: # 当前已经到当前前缀最大了, 除以10相当于回到父节点
                    j //= 10
                j += 1 # 下一个节点
        return ans
