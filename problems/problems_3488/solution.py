import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.solveQueries(*test_input)

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # 预处理：每个值的所有位置
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        # 每个位置到最近同值的最小距离
        dist = [n] * n
        for indices in pos.values():
            k = len(indices)
            if k == 1:
                continue
            for i, idx in enumerate(indices):
                prev_idx = indices[i - 1]
                next_idx = indices[(i + 1) % k]
                # 左边距离：i=0 时环形
                d_left = idx - prev_idx if i > 0 else idx + n - prev_idx
                # 右边距离：i=k-1 时环形
                d_right = next_idx - idx if i < k - 1 else next_idx + n - idx
                dist[idx] = min(d_left, d_right)

        # 查询
        return [dist[q] if dist[q] < n else -1 for q in queries]
