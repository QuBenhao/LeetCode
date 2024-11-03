import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shoppingOffers(*test_input)

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dfs(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]
            res = sum(needs[i] * price[i] for i in range(len(needs)))
            for s in special:
                if all(needs[i] >= s[i] for i in range(len(needs))):
                    res = min(res, s[-1] + dfs([needs[i] - s[i] for i in range(len(needs))]))
            memo[tuple(needs)] = res
            return res

        memo = {}
        return dfs(needs)

