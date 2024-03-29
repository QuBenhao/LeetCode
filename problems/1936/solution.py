import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.addRungs(*test_input)

    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        cur = ans = 0
        for h in rungs:
            ans += (h - cur - 1) // dist
            cur = h
        return ans
