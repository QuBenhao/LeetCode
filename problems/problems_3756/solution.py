import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumAndMultiply(*test_input)

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        pre_sum = [0] * (n + 1)
        nums = [0] * (n + 1)
        non_zero_counts = [0] * (n + 1)
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD
        for i, c in enumerate(s):
            v = int(c)
            pre_sum[i + 1] = pre_sum[i] + v
            non_zero_counts[i + 1] = non_zero_counts[i] + (c != '0')
            nums[i + 1] = nums[i] * 10 % MOD if c != '0' else nums[i] % MOD
            if c != '0':
                nums[i + 1] = (nums[i + 1] + v) % MOD
        ans = []
        for l, r in queries:
            cnt = non_zero_counts[r + 1] - non_zero_counts[l]
            x = (nums[r + 1] - nums[l] * pow10[cnt]) % MOD
            sd = pre_sum[r + 1] - pre_sum[l]
            ans.append(x * sd % MOD)
        return ans

MOD = 10 ** 9 + 7
