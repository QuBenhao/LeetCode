import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.deleteAndEarn(list(test_input))

    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        ns = sorted(cnt.keys())
        # 对当前最大值和上次最大值（延时更新）的动态规划
        dp = [0] * len(cnt)
        max_so_far = dp[0] = cnt[ns[0]] * ns[0]
        max_except_last = 0
        for i in range(1,len(cnt)):
            if ns[i-1] == ns[i] - 1:
                dp[i] = max_except_last
            else:
                dp[i] = max_so_far
            dp[i] += cnt[ns[i]] * ns[i]
            max_except_last = max_so_far
            max_so_far = max(max_so_far, dp[i])
        return max(dp)
