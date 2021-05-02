import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.leastBricks([x[:] for x in test_input])

    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        res = Counter()
        for line in wall:
            start = 0
            for brick in line[:-1]:
                start += brick
                res[start] += 1
        return len(wall) - max(res.values()) if res else len(wall)
