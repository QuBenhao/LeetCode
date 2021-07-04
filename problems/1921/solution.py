import solution
from collections import Counter
from math import ceil


class Solution(solution.Solution):
    def solve(self, test_input=None):
        dist, speed = test_input
        return self.eliminateMaximum(list(dist), list(speed))

    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cnts = Counter()
        for d,s in zip(dist,speed):
            cnts[ceil(d/s)-1] += 1
        ans = 0
        for k in sorted(cnts.keys()):
            if cnts[k] > k + 1 - ans:
                return k + 1
            ans += cnts[k]
        return ans
