import heapq

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.totalCost(*test_input)

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # 存在交叉的情况，可以取k个最小的数
        if candidates * 2 + k > len(costs):
            costs.sort()
            return sum(costs[:k])
        
        # 不存在交叉
        left_idx, right_idx = candidates, -candidates-1
        left, right = costs[:left_idx], costs[right_idx+1:]
        heapq.heapify(left)
        heapq.heapify(right)
        ans = 0
        for _ in range(k):
            if right[0] < left[0]:
                ans += heapq.heapreplace(right, costs[right_idx])
                right_idx -= 1
            else:
                ans += heapq.heapreplace(left, costs[left_idx])
                left_idx += 1
        return ans
