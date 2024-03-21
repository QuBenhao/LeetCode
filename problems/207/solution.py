import solution
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canFinish(*test_input)

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 我们只能从没有prerequire的课程开始
        In = [0] * numCourses
        connect = defaultdict(list)
        for a, b in prerequisites:
            connect[b].append(a)
            In[a] += 1
        q = deque([])
        for i in range(numCourses):
            if not In[i]:
                q.append(i)
        while q:
            i = q.popleft()
            for j in connect[i]:
                In[j] -= 1
                if not In[j]:
                    q.append(j)
        return all(not In[i] for i in range(numCourses))
