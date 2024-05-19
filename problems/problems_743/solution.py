import solution
from collections import defaultdict, deque
import heapq
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.networkDelayTime(*test_input)

    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        connect = defaultdict(lambda:defaultdict(int))
        for u,v,w in times:
            connect[u][v] = w
        q = [(0, k)]
        explored = set()
        while q:
            t, node = heapq.heappop(q)
            if node in explored:
                continue
            explored.add(node)
            if len(explored) == n:
                return t
            for other, tm in connect[node].items():
                if other not in explored:
                    heapq.heappush(q, (t+tm, other))
        return -1

        # connect = defaultdict(lambda:defaultdict(int))
        # for u,v,w in times:
        #     connect[u][v] = w
        # q = deque([k])
        # explored = defaultdict(lambda:inf)
        # explored[k] = 0
        # while q:
        #     node = q.popleft()
        #     t = explored[node]
        #     for other, tm in connect[node].items():
        #         if t + tm < explored[other]:
        #             explored[other] = t + tm
        #             q.append(other)
        # return -1 if len(explored) < n else max(explored.values())
