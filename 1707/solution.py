import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, queries = test_input
        return self.maximizeXor(list(nums),[x[:] for x in queries])

    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
