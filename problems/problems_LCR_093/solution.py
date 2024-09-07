from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lenLongestFibSubseq(test_input)

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n, ans = len(arr), 0
        idx_map = {x: i for i, x in enumerate(arr)}
        dp = defaultdict(lambda: defaultdict(lambda: 2))
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (nxt := arr[i] + arr[j]) in idx_map:
                    dp[j][idx_map[nxt]] = dp[i][j] + 1
                    ans = max(ans, dp[j][idx_map[nxt]])
        return ans
