import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumSwap(test_input)

    def maximumSwap(self, num: int) -> int:
        nums = []
        idxes = [-1] * 10
        i = 0
        x = num
        while x:
            x, digit = divmod(x, 10)
            nums.append(digit)
            if idxes[digit] == -1:
                idxes[digit] = i
            i += 1
        n = len(nums)
        for i in range(n - 1, -1, -1):
            for j in range(9, nums[i], -1):
                if idxes[j] != -1 and idxes[j] < i:
                    nums[i], nums[idxes[j]] = nums[idxes[j]], nums[i]
                    return int("".join(map(str, nums[::-1])))
        return num
