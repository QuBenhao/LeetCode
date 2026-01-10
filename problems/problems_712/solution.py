import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDeleteSum(*test_input)

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        total = sum(map(ord, s1)) + sum(map(ord, s2))
        if m > n:
            m, n, s1, s2 = n, m, s2, s1
        dp = [0] * (m + 1)
        for c in s2:
            v = ord(c)
            pre = 0
            for i in range(m):
                tmp = dp[i + 1]
                if s1[i] == c:
                    # pre是上一轮的dp[i]
                    dp[i + 1] = pre + v
                else:
                    dp[i + 1] = max(dp[i + 1], dp[i])
                pre = tmp
        return total - dp[m] * 2
