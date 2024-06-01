import solution
from typing import *
from functools import lru_cache


@lru_cache(None)
def combination_nums(total):
    if total <= 1:
        return 0
    return total * (total - 1) // 2


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distributeCandies(*test_input)

    def distributeCandies(self, n: int, limit: int) -> int:
        # 总方案数 C n+2 2
        # 一个人超limit的个数为 C n+1-limit 2
        # 两个人超limit的个数为 C n-2*limit 2
        # 三个人超limit的个数为 C n-1-3*limit 2

        return (combination_nums(n + 2)
                - 3 * combination_nums(n + 1 - limit)
                + 3 * combination_nums(n - 2 * limit)
                - combination_nums(n - 1 - 3 * limit)
                )
