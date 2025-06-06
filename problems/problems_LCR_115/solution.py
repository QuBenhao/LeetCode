import solution
from typing import *
from collections import defaultdict, deque
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sequenceReconstruction(*test_input)

    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        graph = defaultdict(set)
        indegree = [0] * n
        for seq in sequences:
            for a, b in pairwise(seq):
                a, b = a - 1, b - 1
                if b not in graph[a]:
                    graph[a].add(b)
                    indegree[b] += 1
        if sum(indegree[i] == 0 for i in range(n)) != 1:
            return False
        for num in nums:
            num -= 1
            if indegree[num] > 0:
                return False
            cnt = 0
            for child in graph[num]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    cnt += 1
            if cnt > 1:
                return False
        return True
