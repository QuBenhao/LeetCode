import solution
from collections import deque, defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        routes, source, target = test_input
        return self.numBusesToDestination([x[:] for x in routes], source, target)

    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        stations = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stations[stop].add(i)
        routes = [set(x) for x in routes]

        q = deque([(source, 0)])
        buses = set()
        stops = {source}
        while q:
            pos, cost = q.popleft()
            if pos == target:
                return cost
            for bus in stations[pos] - buses:
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost + 1))
        return -1
