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
        # 时间，剩余电量, 位置
        heapq.heappush(pq, (0, 0, start))
        # 到每个点，剩余一定电量 所需的最少时间
        dp = set()
        # 优先队列遍历每一个可能的时间点，直到足够到达终点的时间
        while pq:
            t, c, p = heapq.heappop(pq)
            if p == end:
                return t
            # 到达过该点，且比当前的方式快
            if (c, p) in dp:
                continue
            dp.add((c, p))
            # 当前剩余电量不足cnt且没有当前电量+1的状态的话，充一次电入队
            if c < cnt and (c+1, p) not in dp:
                heapq.heappush(pq, (t + charge[p], c + 1, p))
            # 当前电量如果足够前往某个城市，入队
            for nxt in connect[p]:
                dis = connect[p][nxt]
                if dis > c or (c - dis, nxt) in dp:
                    continue
                heapq.heappush(pq, (t + dis, c - dis, nxt))
        return -1
