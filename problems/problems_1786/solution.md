# Python 优先队列

> Author: Benhao
> Date: 2021-03-07
> Upvotes: 1
> Tags: Python

---

### 解题思路
从终点开始推，依次加入到终点距离最短的点，如果距离被计算过，也就说明路径数要叠加之前的点的路径数

### 代码

```python
class Solution(object):
    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        
        connect = [dict() for _ in range(n)]
        
        for e, e_, w in edges:
            connect[e-1][e_-1] = w
            connect[e_-1][e-1] = w

        t = []
        heapq.heappush(t,(0,n-1))
        dis = [float("inf")] * n
        dis[-1] = 0
        ans = [0] * n
        ans[-1] = 1
        visited = [False] * n

        while True:
            curr_dis, node = heapq.heappop(t)
            if node == 0:
                return ans[0] % mod
            if visited[node]:
                continue
            visited[node] = True
            for node_ in connect[node]:
                if not visited[node_]:
                    temp = dis[node] + connect[node_][node]
                    if temp < dis[node_]:
                        dis[node_] = temp
                        heapq.heappush(t, (dis[node_],node_))
                    if dis[node_] > dis[node]:
                        ans[node_] += ans[node]

```