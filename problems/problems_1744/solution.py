import solution
from itertools import accumulate


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canEat(*test_input)

    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Use day + 1 to count elapsed eating days: zero-based day 2 is the third day
        # Minimum days at the fastest rate cap, after eating the preceding presum[ty] candies
        # presum[ty+1] gives the maximum days at the slowest eating rate
        presum = list(accumulate([0] + candiesCount))
        return [presum[t]//c <= d < presum[t+1] for t,d,c in queries]
