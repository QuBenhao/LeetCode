import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.resultArray(*test_input)

    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        cur = [0] * k
        for num in nums:
            m = num % k
            nxt = [0] * k
            for v in range(k):
                if cur[v]:
                    nxt[v * m % k] += cur[v]
            nxt[m] += 1
            cur = nxt
            for v in range(k):
                res[v] += cur[v]
        return res
