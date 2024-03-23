import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxGeneticDifference(*test_input)

    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
