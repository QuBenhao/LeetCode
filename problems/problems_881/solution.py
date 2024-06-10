import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numRescueBoats(*test_input)

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans, left, right = 0, 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            ans += 1
            right -= 1
        return ans
