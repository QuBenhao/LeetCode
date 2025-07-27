from collections import defaultdict, deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minJumps(test_input)

    def minJumps(self, nums: List[int]) -> int:
        graph = defaultdict(list)
        for i, x in enumerate(nums):
            for f in FACTORS[x]:
                graph[f].append(i)
        step = 0
        n = len(nums)
        visited = [False] * n
        visited[0] = True
        q = deque([0])
        while q:
            for _ in range(len(q)):
                i = q.popleft()
                if i == n - 1:
                    return step
                next_indexes = [i + 1]
                if i:
                    next_indexes.append(i - 1)
                if len(FACTORS[nums[i]]) == 1:
                    next_indexes.extend(graph[nums[i]])
                    graph[nums[i]].clear()
                for nxt in next_indexes:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            step += 1
        return step


MAX_N = int(1e6 + 1)
FACTORS = [[] for _ in range(MAX_N)]
for i in range(2, MAX_N):
    if not FACTORS[i]:
        for j in range(i, MAX_N, i):
            FACTORS[j].append(i)
