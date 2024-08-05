import solution
from typing import *
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumRobots(*test_input)

    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        def helper(num) -> bool:
            ans = 0
            q = deque()
            for i in range(n):
                while q and chargeTimes[q[-1]] <= chargeTimes[i]:
                    q.pop()
                q.append(i)
                ans += runningCosts[i]
                if i >= q[0] + num:
                    q.popleft()
                if i + 1 >= num:
                    if ans * num + chargeTimes[q[0]] <= budget:
                        return True
                    ans -= runningCosts[i - num + 1]
            return False

        n = len(chargeTimes)
        left, right = 0, n
        while left < right:
            mid = (left + right + 1) // 2
            if not helper(mid):
                right = mid - 1
            else:
                left = mid
        return left
