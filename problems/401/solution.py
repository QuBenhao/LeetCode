import solution
from itertools import combinations, product
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.readBinaryWatch(turnedOn=test_input)

    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []
        for i in range(min(turnedOn + 1, 4)):
            res += [''.join(p) for p in product(self.hours(i), self.minutes(turnedOn - i))]
        return res

    @lru_cache(None)
    def hours(self, n):
        if not n:
            return ["0:"]
        return [str(s) + ':' for i in combinations([1, 2, 4, 8], n) if 0 <= (s := sum(i)) <= 11]

    @lru_cache(None)
    def minutes(self, n):
        if not n:
            return ["00"]
        ans = []
        for i in combinations([1, 2, 4, 8, 16, 32], n):
            s = sum(i)
            if 0 <= s < 10:
                ans.append('0' + str(s))
            elif s < 60:
                ans.append(str(s))
        return ans
