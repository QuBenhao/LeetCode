import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.twoSum(*test_input)

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur == target:
                break
            elif cur < target:
                left += 1
            else:
                right -= 1
        return [left, right]
