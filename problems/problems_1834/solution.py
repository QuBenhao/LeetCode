import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getOrder([x[:] for x in test_input])

    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        import heapq
        tasks = sorted(enumerate(tasks), key=lambda x: (-x[1][0],-x[1][1],-x[0]))
        ans = []
        pq = []
        time = 0
        while tasks or pq:
            if pq:
                l, idx, t = heapq.heappop(pq)
            else:
                idx, v = tasks.pop()
                t, l = v
            ans.append(idx)
            time = max(t,time) + l
            while tasks and tasks[-1][1][0] <= time:
                index, val = tasks.pop()
                ti, le = val
                heapq.heappush(pq, (le, index, ti))
        return ans
