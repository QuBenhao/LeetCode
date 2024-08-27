from collections import defaultdict
from functools import lru_cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSubstringsInPartition(test_input)

    def minimumSubstringsInPartition(self, s: str) -> int:
        @lru_cache(None)
        def dfs(i):
            if i < 0:
                return 0
            ans = i + 1
            counter = defaultdict(int)
            max_cnt = 0
            for j in range(i, -1, -1):
                counter[s[j]] += 1
                max_cnt = max(max_cnt, counter[s[j]])
                if max_cnt * len(counter) == i - j + 1:
                    ans = min(ans, dfs(j - 1) + 1)
            return ans

        return dfs(len(s) - 1)
