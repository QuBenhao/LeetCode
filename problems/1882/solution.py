import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        servers, tasks = test_input
        return self.assignTasks(list(servers), list(tasks))

    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        ans = []
        pq = []
        for i,s in enumerate(servers):
            heapq.heappush(pq, (s, i))
        use = []
        for base, task in enumerate(tasks):
            while use and use[0][0] <= base:
                _,s,i = heapq.heappop(use)
                heapq.heappush(pq, (s, i))
            if pq:
                s,i = heapq.heappop(pq)
                ans.append(i)
                heapq.heappush(use, (base+task, s, i))
            else:
                t, s, i = heapq.heappop(use)
                ans.append(i)
                heapq.heappush(use, (t + task, s, i))
        return ans
