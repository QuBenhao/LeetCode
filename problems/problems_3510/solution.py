from collections import defaultdict
from heapq import heapify, heappop, heappush
from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumPairRemoval(test_input)

    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        h = []  # (Sum of adjacent elements, index of the left element)
        dec = 0  # Number of decreasing adjacent pairs
        for i, (x, y) in enumerate(pairwise(nums)):
            if x > y:
                dec += 1
            h.append((x + y, i))
        heapify(h)
        lazy = defaultdict(int)

        # Nearest undeleted indices to the left and right of each index
        left = list(range(-1, n))  # Add a sentinel to prevent out-of-bounds indices
        right = list(range(1, n + 1))

        ans = 0
        while dec:
            ans += 1

            while lazy[h[0]]:
                lazy[heappop(h)] -= 1
            s, i = heappop(h)  # Remove the adjacent pair with the smallest sum

            # (Current element, next number)
            nxt = right[i]
            if nums[i] > nums[nxt]:  # Old data
                dec -= 1

            # (Previous number, current element)
            pre = left[i]
            if pre >= 0:
                if nums[pre] > nums[i]:  # Old data
                    dec -= 1
                if nums[pre] > s:  # New data
                    dec += 1
                lazy[(nums[pre] + nums[i], pre)] += 1  # Lazy deletion
                heappush(h, (nums[pre] + s, pre))

            # (Next number, number after next)
            nxt2 = right[nxt]
            if nxt2 < n:
                if nums[nxt] > nums[nxt2]:  # Old data
                    dec -= 1
                if s > nums[nxt2]:  # New data (current element, number after next)
                    dec += 1
                lazy[(nums[nxt] + nums[nxt2], nxt)] += 1  # Lazy deletion
                heappush(h, (s + nums[nxt2], i))

            nums[i] = s
            # Remove nxt
            l, r = left[nxt], right[nxt]
            right[l] = r  # Simulate deletion in a doubly linked list
            left[r] = l

        return ans
