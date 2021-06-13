import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ranges, left, right = test_input
        return self.isCovered([x[:] for x in ranges], left, right)

    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        return all(any(l <= i <= r for l, r in ranges) for i in range(left, right + 1))
