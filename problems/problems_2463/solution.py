import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumTotalDistance(*test_input)

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # 排序：贪心性质，机器人按顺序分配给工厂
        robot.sort()
        factory.sort(key=lambda x: x[0])

        n, m = len(robot), len(factory)

        # 前缀和：prefix[i] = sum(robot[0:i])
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + robot[i]

        # 预处理 cost[l][j] = 机器人 l..n-1 恰好 cnt 个去工厂 j 的距离和
        # 这里用滚动计算，避免额外空间

        # dp[i][j] = 前 i 个机器人分配到前 j 个工厂的最小总距离
        INF = 10**18
        dp = [[INF] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for j in range(1, m + 1):
            pos, limit = factory[j - 1]
            dp[0][j] = 0

            for i in range(1, n + 1):
                # 枚举第 j 个工厂修 cnt 个机器人
                # 机器人 robot[i-cnt] 到 robot[i-1] 去 pos
                dist = 0
                for cnt in range(min(i, limit) + 1):
                    if cnt > 0:
                        # 滚动计算距离，O(1) 增量
                        dist += abs(robot[i - cnt] - pos)
                    if dp[i - cnt][j - 1] != INF:
                        dp[i][j] = min(dp[i][j], dp[i - cnt][j - 1] + dist)

        return dp[n][m]

