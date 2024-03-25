import solution
from typing import *



# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution(solution.Solution):
    def solve(self, test_input=None):
        schedule = test_input
        return self.employeeFreeTime(schedule)

    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
            pass
        