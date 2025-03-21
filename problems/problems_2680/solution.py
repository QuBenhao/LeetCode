import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumOr(*test_input)

    def maximumOr(self, nums: List[int], k: int) -> int:
        all_or = fixed = 0
        for x in nums:
            # 如果在计算 all_or |= x 之前，all_or 和 x 有公共的 1
            # 那就意味着有多个 nums[i] 在这些比特位上都是 1
            fixed |= all_or & x  # 把公共的 1 记录到 fixed 中
            all_or |= x  # 所有数的 OR
        return max((all_or ^ x) | fixed | (x << k) for x in nums)
