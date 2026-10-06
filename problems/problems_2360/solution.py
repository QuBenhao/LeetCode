import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestCycle(test_input)

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        cur_time = 1  # Current time
        vis_time = [0] * n  # Time when x was first visited
        for x in range(n):
            start_time = cur_time  # Start time of this traversal
            while x != -1 and vis_time[x] == 0:  # x has not been visited
                vis_time[x] = cur_time  # Record the time of the visit to x
                cur_time += 1
                x = edges[x]  # Visit the next node
            if x != -1 and vis_time[x] >= start_time:  # Visiting x twice in this traversal means x lies on a cycle
                ans = max(ans, cur_time - vis_time[x])  # The difference between the two visit times is the cycle length
        return ans  # If no cycle is found, return the initial value of ans, -1
