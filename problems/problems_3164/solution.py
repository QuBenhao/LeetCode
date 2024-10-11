from collections import defaultdict
from math import isqrt

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfPairs(*test_input)

    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        counter = defaultdict(int)
        for num in nums1:
            if num % k:
                continue
            num //= k
            for d in range(1, isqrt(num) + 1):
                if num % d:
                    continue
                counter[d] += 1
                if d * d < num:
                    counter[num // d] += 1
        return sum(counter[num] for num in nums2)
