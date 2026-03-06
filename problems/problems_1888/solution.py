from math import inf
import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minFlips(str(test_input))

    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pre01 = [0] * (n + 1)
        pre10 = [0] * (n + 1)
        for i,c in enumerate(s):
            if ord(c) & 1 == i & 1:
                pre10[i + 1] += pre10[i] + 1
                pre01[i + 1] = pre01[i]
            else:
                pre01[i + 1] = pre01[i] + 1
                pre10[i + 1] = pre10[i]
        if n % 2 == 0:
            return min(pre01[-1],pre10[-1])
        ans = inf
        for i in range(n):
            # 把前面i个放到最后
            # 前面要10101，后面要010
            ans1 = pre01[-1] - pre01[i] + pre10[i]
            ans2 = pre10[-1] - pre10[i] + pre01[i]
            ans = min(ans, ans1, ans2)
        return ans
