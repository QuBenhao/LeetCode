import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.earliestAndLatest(*test_input)

    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """

        @lru_cache(None)
        def dp(l, r, m):
            if l > r:
                return dp(r, l, m)
            # The two players reach the same position, meaning they compete
            if l == r:
                return 1, 1

            earliest, latest = m, 0
            # Next l ranges from 1 (everyone before l loses) to l (everyone before l wins)
            for i in range(1, l + 1):
                # Next r ranges from l-i+1 (everyone between r and l loses) to r-i (everyone between them wins)
                for j in range(l - i + 1, r - i + 1):
                    # Use symmetry to avoid some equivalent computations?
                    if not (m + 1) // 2 >= i + j >= l + r - m // 2:
                        continue
                    ea, la = dp(i, j, (m + 1) // 2)
                    earliest = min(earliest, ea)
                    latest = max(latest, la)
            return earliest + 1, latest + 1

        return list(dp(firstPlayer, n - secondPlayer + 1, n))
