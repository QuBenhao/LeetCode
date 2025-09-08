import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.peopleAwareOfSecret(*test_input)

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        pre_sum = [0] * (n + 1)
        pre_sum[1] = 1
        for i in range(2, n + 1):
            inc = pre_sum[max(i - delay, 0)] - pre_sum[max(i - forget, 0)]
            pre_sum[i] = (pre_sum[i - 1] + inc) % MOD
        return (pre_sum[n] - pre_sum[max(n - forget, 0)]) % MOD

MOD = 10**9 + 7
