import solution
from collections import deque, defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.calcEquation(*test_input)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1.0 / val))

        def bfs(init, goal):
            if init not in graph or goal not in graph:
                return -1.0
            explored = {init}
            q = deque([(init, 1.0)])
            while q:
                node, v = q.popleft()
                if node == goal:
                    return v
                for nxt, cost in graph[node]:
                    if nxt not in explored:
                        explored.add(nxt)
                        q.append((nxt, v * cost))
            return -1.0

        return [bfs(i, g) for i, g in queries]
