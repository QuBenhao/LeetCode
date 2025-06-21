from collections import deque
from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.primeSubarray(*test_input)

    def primeSubarray(self, nums: List[int], k: int) -> int:
        q, max_q, min_q = deque(), deque(), deque()
        ans = 0
        left = 0
        for right, num in enumerate(nums):
            if is_primes[num]:
                q.append(right)
                while max_q and nums[max_q[-1]] < num:
                    max_q.pop()
                max_q.append(right)
                while min_q and nums[min_q[-1]] > num:
                    min_q.pop()
                min_q.append(right)
            while q and max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > k:
                left = q.popleft() + 1
                while max_q and max_q[0] < left:
                    max_q.popleft()
                while min_q and min_q[0] < left:
                    min_q.popleft()
            if len(q) >= 2:
                ans += q[-2] - left + 1
        return ans

N = 5 * 10**4
is_primes = [True] * (N + 1)
is_primes[0] = is_primes[1] = False
for i in range(2, N + 1):
    if is_primes[i]:
        for j in range(i*i, N+1, i):
            is_primes[j] = False
