import solution
from math import ceil


class Solution(solution.Solution):
    def solve(self, test_input=None):
        dist, speed, hoursBefore = test_input
        return self.minSkips(list(dist), speed, hoursBefore)

    def minSkips(self, dist, speed, hoursBefore):
        """
        :type dist: List[int]
        :type speed: int
        :type hoursBefore: int
        :rtype: int
        """
        # 解决精度问题 ceil(8.0+1.0/3+1.0/3+1.0/3) = 10 而不是 9
        eps = 1e-9
        n = len(dist)
        # 只要一个比到达时间大的数即可，使用float("inf")需要在后面加法中特判，比较麻烦
        dp = [[10 ** 7 + 1] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i, d in enumerate(dist, 1):
            # 全都不跳跃
            dp[i][0] = ceil(dp[i - 1][0] + d / speed - eps)
            # 到i的时候最多跳跃i次
            for j in range(1, i + 1):
                # 跳跃j次是 本次跳跃，上次跳了j-1次 和 本次不跳跃，上次跳了j次 的递推
                dp[i][j] = min(dp[i - 1][j - 1] + d / speed, ceil(dp[i - 1][j] + d / speed - eps))

        for j, t in enumerate(dp[-1]):
            # 从左到右，最小的满足时间内到达的跳跃次数
            if t <= hoursBefore:
                return j
        return -1
