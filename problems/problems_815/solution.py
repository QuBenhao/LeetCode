import solution
from collections import deque, defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numBusesToDestination(*test_input)

    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        # 每个车站可以乘坐的公交车
        stations = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stations[stop].add(i)
        # 每个公交车线路可以到达的车站
        routes = [set(x) for x in routes]

        q = deque([(source, 0)])
        # 已经乘坐了的公交车
        buses = set()
        # 已经到达了的车站
        stops = {source}
        while q:
            pos, cost = q.popleft()
            if pos == target:
                return cost
            # 当前车站中尚未乘坐的公交车
            for bus in stations[pos] - buses:
                buses.add(bus)
                # 该公交车尚未到达过的车站
                for s in routes[bus] - stops:
                    stops.add(s)
                    q.append((s, cost + 1))
        return -1
