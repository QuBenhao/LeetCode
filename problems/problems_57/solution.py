import solution
from typing import *
from bisect import bisect_left, bisect_right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.insert(*test_input)

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l_idx = bisect_left(intervals, newInterval[0], key=lambda x: x[1])
        r_idx = bisect_right(intervals, newInterval[1], key=lambda x: x[0]) - 1
        return intervals[:l_idx] + [
            [min(intervals[l_idx][0], newInterval[0]), max(intervals[r_idx][1], newInterval[1])]] + intervals[
                                                                                                    r_idx + 1:] if l_idx < len(
            intervals) and r_idx >= 0 else (
            intervals + [newInterval] if l_idx == len(intervals) else [newInterval] + intervals)
