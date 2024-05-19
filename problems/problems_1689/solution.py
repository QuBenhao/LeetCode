import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minPartitions(test_input)

    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return max([int(char) for char in n])
