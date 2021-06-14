import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, firstPlayer, secondPlayer = test_input
        return self.earliestAndLatest(n, firstPlayer, secondPlayer)

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
            # 两个人到达同一位置(即他俩发生了对抗)
            if l == r:
                return 1, 1

            earliest, latest = m, 0
            # l的下一个可能性为1(l前面的全部为负)到l(l前面的全部为胜)
            for i in range(1, l + 1):
                # r的下一个可能性为l-i+1 (r到l之间的全部为负)到r-i (r到l之间的全部为胜)
                for j in range(l - i + 1, r - i + 1):
                    # 根据对称性省去一些不必要的等价求解?
                    if not (m + 1) // 2 >= i + j >= l + r - m // 2:
                        continue
                    ea, la = dp(i, j, (m + 1) // 2)
                    earliest = min(earliest, ea)
                    latest = max(latest, la)
            return earliest + 1, latest + 1

        return list(dp(firstPlayer, n - secondPlayer + 1, n))
