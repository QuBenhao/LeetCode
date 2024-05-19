import solution
from typing import *
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isInterleave(*test_input)

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 + len2 != len(s3):
            return False

        @lru_cache(None)
        def dfs(idx1, idx2):
            return True if idx1 == len1 and idx2 == len2 \
                else ((idx1 < len1 and s1[idx1] == s3[idx1 + idx2] and dfs(idx1 + 1, idx2))
                      or (idx2 < len2 and s2[idx2] == s3[idx1 + idx2] and dfs(idx1, idx2 + 1)))

        return dfs(0, 0)
