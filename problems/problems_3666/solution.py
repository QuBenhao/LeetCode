from math import inf

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        if z == 0:
            return 0
        if k == n:
            return 1 if z == n else -1

        ans = inf
        # Case 1: the operation count m is even
        if z % 2 == 0:  # z must be even
            m = max((z + k - 1) // k, (z + n - k - 1) // (n - k))  # Lower bound
            ans = m + m % 2  # Round m up to an even number

        # Case 2: the operation count m is odd
        if z % 2 == k % 2:  # z and k must have the same parity
            m = max((z + k - 1) // k, (n - z + n - k - 1) // (n - k))  # Lower bound
            ans = min(ans, m | 1)  # Round m up to an odd number

        return ans if ans < inf else -1
