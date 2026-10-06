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
            # If the entire subtree contains fewer nodes than needed, skip it and move to the next node at this level (for example, 1 -> 2)
            if count < k:
                k -= count
                cur += 1 # to go to the next number
            # The answer is among the current node's descendants; consume the root and descend with DFS (for example, 1 -> 10)
            else:
                k -= 1
                cur *= 10 # to go deeper in the tree
        return cur
