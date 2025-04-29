import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findNumbers(test_input)

    def findNumbers(self, nums: List[int]) -> int:
        def count_digits(n: int) -> int:
            count = 0
            while n > 0:
                n //= 10
                count += 1
            return count

        return sum(count_digits(num) % 2 == 0 for num in nums)

