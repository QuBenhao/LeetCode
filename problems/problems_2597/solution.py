from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.beautifulSubsets(*test_input)

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = defaultdict(Counter)
        for x in nums:
            # Group values with the same remainder modulo k, recording each value x and its frequency
            groups[x % k][x] += 1

        ans = 1
        for cnt in groups.values():
            # Compute the number of ways for this group
            a = sorted(cnt.items())
            m = len(a)
            f = [0] * (m + 1)
            f[0] = 1
            f[1] = 1 << a[0][1]
            for i in range(1, m):
                if a[i][0] - a[i - 1][0] == k:
                    f[i + 1] = f[i] + f[i - 1] * ((1 << a[i][1]) - 1)
                else:
                    f[i + 1] = f[i] << a[i][1]
            ans *= f[m]  # Multiply the number of ways across groups
        return ans - 1  # Exclude the empty set
