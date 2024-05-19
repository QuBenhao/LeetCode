import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.totalHammingDistance(list(test_input))

    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum((ones := s.count('1')) * (len(nums) - ones) for s in zip(*map('{:30b}'.format, nums)))
