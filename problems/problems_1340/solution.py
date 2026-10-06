import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxJumps(*test_input)

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        # Precompute with a monotonic stack: the nearest barrier on either side whose height is >= the current height
        # right[i] = the first index j to the right of i with arr[j] >= arr[i], or n if none exists
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                right[stack.pop()] = i
            stack.append(i)

        # left[i] = the first index j to the left of i with arr[j] >= arr[i], or -1 if none exists
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # DP: process heights in ascending order
        indices = sorted(range(n), key=lambda i: arr[i])
        dp = [1] * n

        for i in indices:
            lo = max(left[i] + 1, i - d)
            hi = min(right[i] - 1, i + d)
            for j in range(lo, hi + 1):
                if j != i:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

