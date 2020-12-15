import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sortedSquares(test_input)

    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(num**2 for num in nums)
