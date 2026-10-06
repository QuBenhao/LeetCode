import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.solveQueries(*test_input)

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        # Preprocess: all positions of each value
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)

        # Minimum distance from each position to the nearest equal value
        dist = [n] * n
        for indices in pos.values():
            k = len(indices)
            if k == 1:
                continue
            for i, idx in enumerate(indices):
                prev_idx = indices[i - 1]
                next_idx = indices[(i + 1) % k]
                # Distance to the left: wrap around when i=0
                d_left = idx - prev_idx if i > 0 else idx + n - prev_idx
                # Distance to the right: wrap around when i=k-1
                d_right = next_idx - idx if i < k - 1 else next_idx + n - idx
                dist[idx] = min(d_left, d_right)

        # Queries
        return [dist[q] if dist[q] < n else -1 for q in queries]
