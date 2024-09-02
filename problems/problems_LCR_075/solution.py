import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.relativeSortArray(*test_input)

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        c = Counter(arr1)
        ans = []
        for num in arr2:
            ans.extend([num] * c[num])
            c.pop(num)
        for num in sorted(c.keys()):
            ans.extend([num] * c[num])
        return ans
