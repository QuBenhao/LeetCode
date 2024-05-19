import solution
from typing import *
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDivScore(*test_input)

    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        nums.sort(reverse=True)
        dup = sum(1 for x, y in pairwise(nums) if x == y)
        divisors.sort()
        max_cnt, ans = -1, 0
        for d in divisors:
            if (max_cnt - dup + 1) * d > nums[0]:
                break
            cnt = 0
            for x in nums:
                if x < d:
                    break
                if x % d == 0:
                    cnt += 1
            if cnt > max_cnt:
                max_cnt, ans = cnt, d
        return ans

