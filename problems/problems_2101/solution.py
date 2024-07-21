import solution
from typing import *
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumDetonation(test_input)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n - 1):
            x1, y1, r1 = bombs[i]
            r1 *= r1
            for j in range(i + 1, n):
                x2, y2, r2 = bombs[j]
                dis = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dis <= r1:
                    graph[i].append(j)
                if dis <= r2 * r2:
                    graph[j].append(i)

        ans = 0
        for i in range(n):
            q, cur, explored = deque([i]), 0, {i}
            while q:
                node = q.popleft()
                cur += 1
                for nxt in graph[node]:
                    if nxt not in explored:
                        explored.add(nxt)
                        q.append(nxt)
            ans = max(ans, cur)
        return ans
