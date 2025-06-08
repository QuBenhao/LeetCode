import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findKthNumber(*test_input)

    def findKthNumber(self, n: int, k: int) -> int:
        def dfs(l, r):
            if l > n:
                return 0
            return min(n, r) - l + 1 + dfs(l * 10, r * 10 + 9)

        cur = 1
        while k > 1:
            count = dfs(cur, cur)
            # 当前节点中总数都小于需要的数，可以全部取走，bfs到同层下一点 (比如 1 -> 2)
            if count < k:
                k -= count
                cur += 1 # to go to the next number
            # 答案在当前节点的子节点中，取走当前根节点，dfs向下 (比如 1 -> 10)
            else:
                k -= 1
                cur *= 10 # to go deeper in the tree
        return cur
