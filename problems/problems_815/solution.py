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
        # Bus routes available at each stop
        stations = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stations[stop].add(i)
        # Stops reachable on each bus route
        routes = [set(x) for x in routes]

        q = deque([(source, 0)])
        # Bus routes already taken
        buses = set()
        # Stops already reached
        stops = {source}
        while q:
            pos, cost = q.popleft()
            if pos == target:
                return cost
            # Bus routes at the current stop that have not yet been taken
            for bus in stations[pos] - buses:
                buses.add(bus)
                # Stops on this bus route that have not yet been reached
                for s in routes[bus] - stops:
                    stops.add(s)
                    q.append((s, cost + 1))
        return -1
