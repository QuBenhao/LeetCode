import solution
import bisect, heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minInterval(*test_input)

    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # Priority queue
        intervals.sort(reverse=True)
        pq = []
        res = {}
        for q in sorted(queries):
            # Start checking from the smallest left endpoint
            while intervals and intervals[-1][0] <= q:
                l, r = intervals.pop()
                # The right endpoint satisfies the condition
                if r >= q:
                    heapq.heappush(pq,(r-l+1,r))
            # Remove entries from pq whose right endpoints fail the condition
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            res[q] = pq[0][0] if pq else -1
        return [res[q] for q in queries]

        # # Union-find solution
        # n = len(queries)
        # q = sorted(queries)
        # intervals.sort(key=lambda x:x[1]-x[0])
        # ans = [-1] * n
        # par = list(range(n+1))
        #
        # def find(x):
        #     if par[x] != x:
        #         par[x] = find(par[x])
        #     return par[x]
        #
        # for a, b in intervals:
        #     l,r = bisect.bisect_left(q, a), bisect.bisect_right(q, b)
        #     # Use union-find to find the next position
        #     v = find(l)
        #     while v < r:
        #         ans[v] = b - a + 1
        #         par[v] = v + 1
        #         v = find(v)
        #
        # d = {val:i for i,val in enumerate(q)}
        # return [ans[d[i]] for i in queries]
