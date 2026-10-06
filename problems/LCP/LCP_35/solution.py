import solution
from collections import defaultdict
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        paths, cnt, start, end, charge = test_input
        return self.electricCarPlan([x[:] for x in paths], cnt, start, end, list(charge))

    def electricCarPlan(self, paths, cnt, start, end, charge):
        """
        :type paths: List[List[int]]
        :type cnt: int
        :type start: int
        :type end: int
        :type charge: List[int]
        :rtype: int
        """
        connect = defaultdict(dict)
        for a, b, w in paths:
            if a in connect and b in connect[a]:
                connect[a][b] = connect[b][a] = min(w, connect[a][b])
            else:
                connect[a][b] = connect[b][a] = w
        pq = []
        # Time, remaining charge, position
        heapq.heappush(pq, (0, 0, start))
        # Minimum time to reach each node with a given remaining charge
        dp = set()
        # Explore candidate arrival times with a priority queue until the destination is reached
        while pq:
            t, c, p = heapq.heappop(pq)
            if p == end:
                return t
            # This node was already reached faster with the same remaining charge
            if (c, p) in dp:
                continue
            dp.add((c, p))
            # If the remaining charge is below cnt and the state with one more unit of charge is unvisited, charge once and enqueue
            if c < cnt and (c+1, p) not in dp:
                heapq.heappush(pq, (t + charge[p], c + 1, p))
            # If the current charge is enough to reach a city, enqueue that move
            for nxt in connect[p]:
                dis = connect[p][nxt]
                if dis > c or (c - dis, nxt) in dp:
                    continue
                heapq.heappush(pq, (t + dis, c - dis, nxt))
        return -1
