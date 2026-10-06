import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumSumSubsequence(*test_input)

    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        # The four values store f00, f01, f10, and f11
        t = [[0] * 4 for _ in range(2 << n.bit_length())]

        # A handwritten max is more efficient
        def max(a: int, b: int) -> int:
            return b if b > a else a

        # Merge the left and right children
        def maintain(o: int):
            a, b = t[o * 2], t[o * 2 + 1]
            t[o][0] = max(a[0] + b[2], a[1] + b[0])
            t[o][1] = max(a[0] + b[3], a[1] + b[1])
            t[o][2] = max(a[2] + b[2], a[3] + b[0])
            t[o][3] = max(a[2] + b[3], a[3] + b[1])

        # Initialize the segment tree with nums
        def build(o: int, l: int, r: int) -> None:
            if l == r:
                t[o][3] = max(nums[l], 0)
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            maintain(o)

        # Set nums[i] to val
        def update(o: int, l: int, r: int, i: int, val: int) -> None:
            if l == r:
                t[o][3] = max(val, 0)
                return
            m = (l + r) // 2
            if i <= m:
                update(o * 2, l, m, i, val)
            else:
                update(o * 2 + 1, m + 1, r, i, val)
            maintain(o)

        build(1, 0, n - 1)

        ans = 0
        for i, x in queries:
            update(1, 0, n - 1, i, x)
            ans += t[1][3]  # f11 has no restrictions, so it is the House Robber problem on the entire array
        return ans % 1_000_000_007
