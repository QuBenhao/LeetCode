import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxScore(list(test_input))

    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        try:
            from math import gcd
        except:
            from fractions import gcd

        n = len(nums)
        dp = [-1] * (1 << n)

        def dfs(mask, t):
            if mask == (1 << n) - 1:
                return 0
            if dp[mask] != -1:
                return dp[mask]
            ma = 0
            for i in range(n):
                if (1 << i) & mask:
                    continue
                for j in range(i + 1, n):
                    if (1 << j) & mask:
                        continue
                    next = dfs(mask | (1 << i) | (1 << j), t + 1) + gcd(nums[i], nums[j]) * t
                    ma = max(next, ma)
            dp[mask] = ma
            return dp[mask]

        return dfs(0, 1)
