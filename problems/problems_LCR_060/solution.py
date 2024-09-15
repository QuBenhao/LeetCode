import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.topKFrequent(*test_input)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in counter.most_common(k)] if (counter := Counter(nums)) else []
