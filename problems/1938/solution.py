import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxGeneticDifference(list(test_input[0]), [x[:] for x in test_input[1]])

    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
