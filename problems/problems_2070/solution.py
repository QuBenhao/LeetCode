from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumBeauty(*test_input)

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda item: item[0])
        idx = sorted(range(len(queries)), key=lambda i: queries[i])

        ans = [0] * len(queries)
        max_beauty = j = 0
        for i in idx:
            q = queries[i]
            # 增量地遍历满足 queries[i-1] < price <= queries[i] 的物品
            while j < len(items) and items[j][0] <= q:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            ans[i] = max_beauty
        return ans
