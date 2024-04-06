import solution
from typing import *
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getAncestors(*test_input)

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph, direct, ans = defaultdict(list), [0] * n, [set() for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            direct[b] += 1
        q = deque([])
        for i in range(n):
            if direct[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for child in graph[node]:
                ans[child].update(ans[node])
                ans[child].add(node)
                direct[child] -= 1
                if direct[child] == 0:
                    q.append(child)
        return [list(sorted(s)) for s in ans]
