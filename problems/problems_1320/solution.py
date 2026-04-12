import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDistance(test_input)

    def minimumDistance(self, word: str) -> int:
        def dist(a: int, b: int) -> int:
            if a < 0 or b < 0:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        INF = float('inf')
        dp = {(-1, -1): 0}  # (pos1, pos2), -1表示未放置，保证pos1 <= pos2

        for ch in word:
            cur = ord(ch) - ord('A')
            new_dp = {}
            for (p1, p2), cost in dp.items():
                # 尝试用两根手指分别移动到cur
                for old_pos, new_pos in [(p1, p2), (p2, p1)]:
                    new_p1, new_p2 = sorted([new_pos, cur])
                    move_cost = dist(old_pos, cur) if old_pos >= 0 else 0
                    key = (new_p1, new_p2)
                    new_dp[key] = min(new_dp.get(key, INF), cost + move_cost)
            dp = new_dp

        return min(dp.values())
