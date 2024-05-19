import solution
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDays(*test_input)

    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def can_make(days):
            flowers = blooms = 0
            for day in bloomDay:
                if day <= days:
                    blooms += 1
                    if blooms == k:
                        flowers += 1
                        if flowers == m:
                            return True
                        blooms = 0
                else:
                    blooms = 0
            return False

        if m * k > len(bloomDay):
            return -1
        left, right = m * k, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if can_make(mid):
                right = mid
            else:
                left = mid + 1
        return right
