import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.intersectionSizeTwo(test_input)

    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort right endpoints in ascending order to make greedy endpoint selection valid; break ties with the shortest interval, which has the fewest choices and whose selected points also cover the other intervals
        intervals.sort(key=lambda x: (x[1], -x[0]))
        # Since elements are added in increasing order, the two largest elements suffice to decide whether to add more
        a, b, ans = -1, -1, 0
        for left, right in intervals:
            # If the left endpoint is beyond the current largest element, add two new points from this interval (view this recursively: earlier points no longer matter)
            if left > b:
                # Greedily take the two largest points
                a, b, ans = right - 1, right, ans + 2
            # If the left endpoint lies between the two largest elements, the largest element is already a point in this interval
            elif left > a:
                # We need one more point; greedily take this interval's largest point, making the old b the second largest
                a, b, ans = b, right, ans + 1
        return ans
