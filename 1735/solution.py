import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToFillArray([x[:] for x in test_input])

    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
