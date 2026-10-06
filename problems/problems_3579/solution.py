from collections import defaultdict
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, word1: str, word2: str) -> int:
        def update(counter, x, y):
            if x == y:
                return
            if counter[(y, x)] > 0:
                counter[(y, x)] -= 1
                # A reverse pair was found, so replace the previous replacement operation with a swap; the operation count stays unchanged
            else:
                counter[(x, y)] += 1
                nonlocal op
                op += 1 # Use a replacement operation for now

        n = len(word1)

        # Preprocess all substrings for reversal operations
        rev_op = [[0] * n for _ in range(n)]
        # Expand around the center
        for i in range(2 * n - 1):
            cnt = defaultdict(int)
            op = 1 # Reversal operation
            l, r = i // 2, (i+1) // 2
            while l >= 0 and r < n:
                update(cnt, word1[l], word2[r])
                if l != r:
                    update(cnt, word1[r], word2[l])
                rev_op[l][r] = op
                l -= 1
                r += 1

        f = [0] * (n + 1)
        for i in range(n):
            res = inf
            cnt = defaultdict(int)
            op = 0 # Keep the original order without a reversal
            for j in range(i, -1, -1):
                update(cnt, word1[j], word2[j])
                res = min(res, f[j] + min(op, rev_op[j][i])) # Minimum operations for substring [j, i]
            f[i + 1] = res
        return f[n]
