import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findOriginalArray(test_input)

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        zeros = counter.pop(0, 0)
        if zeros % 2 != 0:
            return []
        ans = [0] * (zeros // 2)
        for x in counter:
            if x % 2 == 0 and x // 2 in counter:
                continue
            while x in counter:
                count_x = counter[x]
                if count_x > counter[x * 2]:
                    return []
                ans.extend([x] * count_x)
                if count_x < counter[x * 2]:
                    counter[x * 2] -= count_x
                    x *= 2
                else:
                    x *= 4
        return ans
