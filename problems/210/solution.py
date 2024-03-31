import solution
from typing import *
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findOrder(*test_input)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        In = [0] * numCourses
        connect = defaultdict(set)
        for a, b in prerequisites:
            connect[b].add(a)
            In[a] += 1
        q = deque([])
        for i in range(numCourses):
            if not In[i]:
                q.append(i)
        ans = []
        while q:
            i = q.popleft()
            ans.append(i)
            for j in connect[i]:
                In[j] -= 1
                if not In[j]:
                    q.append(j)
        return ans if len(ans) == numCourses else []
