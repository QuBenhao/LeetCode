import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSetSize(test_input)

    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        n = len(arr)
        cur = n
        ans = 0
        sorted_counter = sorted(counter.items(), key=lambda x: -x[1])
        while cur > n // 2:
            cur -= sorted_counter[ans][1]
            ans += 1
        return ans
