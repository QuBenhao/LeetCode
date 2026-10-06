# [Python] BFS treating each bus route as a whole

> Author: Benhao
> Date: 2021-06-28
> Upvotes: 50
> Tags: Python, Python3

---

### Approach
If you could already take route 1, there is no point taking a detour (route 10 -> route 2 -> route 1) to board it later; boarding it earlier is better.
Record all bus routes available at each step, mark all their stops as reached, and enqueue those stops.

### Code

```python3
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
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
                # Stops on this bus route that have not yet been reached
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost + 1))
        return -1
```
