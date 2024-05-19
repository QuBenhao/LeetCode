import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findCenter([x[:] for x in test_input])

    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        return (set(edges[0]) & set(edges[1])).pop()
