import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countRestrictedPaths(*test_input)

    def countRestrictedPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        import heapq

        connect = [dict() for _ in range(n)]
        for e, e_, w in edges:
            connect[e - 1][e_ - 1] = w
            connect[e_ - 1][e - 1] = w

        t = []
        heapq.heappush(t, (0, n - 1))
        dis = [float("inf")] * n
        dis[-1] = 0
        ans = [0] * n
        ans[-1] = 1
        visited = [False] * n

        while True:
            curr_dis, node = heapq.heappop(t)
            if node == 0:
                return ans[0] % (10 ** 9 + 7)
            if visited[node]:
                continue
            visited[node] = True
            for node_ in connect[node]:
                if not visited[node_]:
                    temp = dis[node] + connect[node_][node]
                    if temp < dis[node_]:
                        dis[node_] = temp
                        heapq.heappush(t, (dis[node_], node_))
                    if dis[node_] > dis[node]:
                        ans[node_] += ans[node]
