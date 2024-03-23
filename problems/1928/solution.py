import solution
from collections import defaultdict
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, maxTime, edges, passingFees):
        """
        :type maxTime: int
        :type edges: List[List[int]]
        :type passingFees: List[int]
        :rtype: int
        """
        n = len(passingFees)
        connect = defaultdict(lambda:defaultdict(lambda:1001))
        for a,b,t in edges:
            connect[a][b] = min(connect[a][b], t)
            connect[b][a] = min(connect[b][a], t)
        # fee, time, pos
        q = [(passingFees[0], maxTime, 0)]
        explored = {0:maxTime}
        while q:
            f, t, pos = heapq.heappop(q)
            if pos == n - 1:
                return f
            for nxt,tm in connect[pos].items():
                if tm > t:
                    continue
                if nxt not in explored or t - tm > explored[nxt]:
                    explored[nxt] = t - tm
                    heapq.heappush(q, (f + passingFees[nxt], t - tm, nxt))
        return -1
