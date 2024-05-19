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
        # 拓扑排序，我们只能从没有prerequire的课程开始
        graph, q, degree = defaultdict(list), deque([]), [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            degree[v] += 1
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        explored = 0
        while q:
            course = q.popleft()
            explored += 1
            for nxt in graph[course]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    q.append(nxt)
        return explored == numCourses
