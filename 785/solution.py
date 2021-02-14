import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isBipartite([x[:] for x in test_input])

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        colored = {}
        for node in range(len(graph)):
            if node not in colored:
                colored[node] = 1
                q = deque([node])
                while q:
                    cur = q.popleft()
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = - colored[cur]
                            q.append(nb)
                        elif colored[nb] == colored[cur]:
                            return False
        return True
