from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.groupThePeople(test_input)

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = defaultdict(list)
        for i, gs in enumerate(groupSizes):
            if gs not in ans or len(ans[gs][-1]) == gs:
                ans[gs].append([])
            ans[gs][-1].append(i)
        return [group for groups in ans.values() for group in groups]
