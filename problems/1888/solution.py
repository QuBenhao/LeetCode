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
        pre01 = [0] * n
        pre10 = [0] * n
        for i,c in enumerate(s):
            if c == '1':
                if i % 2 == 0:
                    pre01[i] = pre01[i-1] + 1
                    pre10[i] = pre10[i-1]
                else:
                    pre10[i] += pre10[i-1] + 1
                    pre01[i] = pre01[i-1]
            else:
                if i % 2 == 0:
                    pre10[i] += pre10[i-1] + 1
                    pre01[i] = pre01[i-1]
                else:
                    pre01[i] = pre01[i-1] + 1
                    pre10[i] = pre10[i-1]
        pre01 = [0] + pre01
        pre10 = [0] + pre10
        if n % 2 == 0:
            return min(pre01[-1],pre10[-1])
        ans = float("inf")
        for i in range(n):
            # 把前面i个放到最后
            # 前面要10101，后面要010
            ans1 = pre01[-1] - pre01[i] + pre10[i]
            ans2 = pre10[-1] - pre10[i] + pre01[i]
            ans = min(ans, ans1, ans2)
        return ans
