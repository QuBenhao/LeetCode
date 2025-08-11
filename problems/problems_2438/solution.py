from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.productQueries(*test_input)

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        pre_sum = [0]
        while n:
            low_bit = n & -n
            pre_sum.append(pre_sum[-1] + low_bit.bit_length() - 1)
            n ^= low_bit
        return [POWERS[pre_sum[j+1] - pre_sum[i]] for i, j in queries]

MOD = 10**9 + 7
# sum(range(31)) = 435
POWERS = [1] * 436
for _i in range(1, 436):
    POWERS[_i] = (POWERS[_i - 1] * 2) % MOD
