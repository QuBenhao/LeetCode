from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPartitions(*test_input)

    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD =  10**9 + 7
        n = len(nums)
        min_q = deque() # Monotonically increasing deque maintaining the window minimum
        max_q = deque() # Monotonically decreasing deque maintaining the window maximum
        f = [0] * (n+1) # f[i] is the number of valid partitions of the subarray ending at nums[i-1]
        f[0] = 1 # Initial state: the empty array has 1 partition
        sum_f = 0 # Track the sum of valid partition counts within the current window
        left = 0

        for i, x in enumerate(nums):
            sum_f += f[i] # Accumulated valid partition count for the current sliding window

            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(i)

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(i)

            while nums[max_q[0]] - nums[min_q[0]] > k: # If the window maximum minus minimum exceeds k, move the left endpoint
                sum_f -= f[left]
                left += 1
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()

            f[i + 1] = sum_f % MOD

        return f[n] % MOD
