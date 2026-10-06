# [Python] BFS + priority queue

> slug: python-bfs-you-xian-dui-lie-by-himymben-qfnk
> date: 2022-01-23
> tags: Python, Python3
> question: K Highest Ranked Items Within a Price Range (k-highest-ranked-items-within-a-price-range)
> url: https://leetcode.cn/problems/k-highest-ranked-items-within-a-price-range/solutions/lPUVRF/python-bfs-you-xian-dui-lie-by-himymben-qfnk/

---
### Approach
Maintain a priority queue of size k while running BFS.

### Code

```python3
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        nodes = [start]
        explored = {tuple(start)}
        cost = 0
        pq = []
        while nodes:
            nxt = []
            for n in nodes:
                if pricing[0] <= grid[n[0]][n[1]] <= pricing[1]:
                    heapq.heappush(pq, (-cost, -grid[n[0]][n[1]], -n[0], -n[1]))
                    if len(pq) > k:
                        heapq.heappop(pq)
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    if 0 <= (nx := n[0] + dx) < len(grid) and 0 <= (ny := n[1] + dy) < len(grid[0]) and (nx, ny) not in explored and grid[nx][ny]:
                        nxt.append((nx, ny))
                        explored.add((nx, ny))
            nodes = nxt
            cost += 1
        ans = []
        while pq:
            _, _, i, j = heapq.heappop(pq)
            ans.append([-i, -j])
        return ans[::-1]

```
