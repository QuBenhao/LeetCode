import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumScore(*test_input)

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        next_greater_right = [n] * n
        next_greater_left = [-1] * n
        cds = [omega[num] for num in nums]

        stack = []
        for i, cd in enumerate(cds):
            while stack and cds[stack[-1]] < cd:
                next_greater_right[stack.pop()] = i
            if stack:
                next_greater_left[i] = stack[-1]
            stack.append(i)

        ans = 1
        ordered = sorted(range(n), key=lambda x: -nums[x])
        for i in ordered:
            if nums[i] == 1:
                break
            right = next_greater_right[i]
            left = next_greater_left[i]
            take = min(k, (right - i) * (i - left))
            ans = (ans * pow(nums[i], take, MOD)) % MOD
            k -= take
            if not k:
                break
        return ans


MOD = 10 ** 9 + 7
MX = 10 ** 5 + 1
omega = [0] * MX
for _i in range(2, MX):
    if omega[_i] == 0:  # _i is prime
        for _j in range(_i, MX, _i):
            omega[_j] += 1 # _i is a prime factor of _j
