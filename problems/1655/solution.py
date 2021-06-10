import solution
from collections import Counter
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, quantity = test_input
        return self.canDistribute(list(nums), list(quantity))

    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        c = Counter(nums)
        m = len(quantity)
        options = [val for val in c.values()]
        options.sort(reverse=True)

        @lru_cache(None)
        def dfs(idx, ops):
            if idx == m:
                return True
            if ops[0] < quantity[idx]:
                return False

            for i in range(len(ops)):
                if ops[i] < quantity[idx]:
                    break
                temp = list(ops)
                temp[i] -= quantity[idx]
                temp.sort(reverse=True)
                if dfs(idx + 1, tuple(temp)):
                    return True
            return False

        return dfs(0, tuple(options[:m]))
