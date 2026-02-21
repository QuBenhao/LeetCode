from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPrimeSetBits(*test_input)

    def countPrimeSetBits(self, left: int, right: int) -> int:
        # return sum(i.bit_count() in PRIMES for i in range(left, right + 1))
        return digitDP(left, right)

PRIMES = {2, 3, 5, 7, 11, 13, 17, 19}
# 代码示例：返回 [low, high] 中的恰好包含 target 个 0 的数字个数
# 比如 digitDP(0, 10, 1) == 2
# 要点：我们统计的是 0 的个数，需要区分【前导零】和【数字中的零】，前导零不能计入，而数字中的零需要计入
def digitDP(low: int, high: int) -> int:
    low_s = list(map(int, bin(low)[2:]))  # 避免在 dfs 中频繁调用 int()
    high_s = list(map(int, bin(high)[2:]))
    n = len(high_s)
    diff_lh = n - len(low_s)

    @cache
    def dfs(i: int, cnt0: int, limit_low: bool, limit_high: bool) -> int:
        if i == n:
            return 1 if cnt0 in PRIMES else 0

        lo = low_s[i - diff_lh] if limit_low and i >= diff_lh else 0
        hi = high_s[i] if limit_high else 1

        res = 0
        start = lo

        # 通过 limit_low 和 i 可以判断能否不填数字，无需 is_num 参数
        # 如果前导零不影响答案，去掉这个 if block
        if limit_low and i < diff_lh:
            # 不填数字，上界不受约束
            res = dfs(i + 1, 0, True, False)
            start = 1

        for d in range(start, hi + 1):
            res += dfs(i + 1,
                       cnt0 + (1 if d == 1 else 0),  # 统计 1 的个数
                       limit_low and d == lo,
                       limit_high and d == hi)

        # res %= MOD
        return res

    return dfs(0, 0, True, True)
