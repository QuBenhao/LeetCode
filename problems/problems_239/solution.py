import solution
from typing import *
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSlidingWindow(*test_input)

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for i, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(i)
            if i >= q[0] + k:
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans
