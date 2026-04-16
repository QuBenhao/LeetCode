# [Python] BFS 把公交看做整体

> Author: Benhao
> Date: 2021-06-28
> Upvotes: 50
> Tags: Python, Python3

---

### 解题思路
你之前可以坐一号线了，你后面兜兜转转(十号线->二号线->一号线)再上一号线是没有意义的(之前上一号线是比这样更优的)。
所以直接记录我们每次能坐的所有公交车，将它的所有站都标记为已到达(且加入队列)。

### 代码

```python3
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
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
                # 该公交车尚未到达过的车站
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost + 1))
        return -1
```