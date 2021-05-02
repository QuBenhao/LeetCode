import solution
import bisect, heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        intervals, queries = test_input
        return self.minInterval([x[:] for x in intervals], list(queries))

    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        # 优先队列
        intervals.sort(reverse=True)
        pq = []
        res = {}
        for q in sorted(queries):
            # 从左边界最小的开始检查
            while intervals and intervals[-1][0] <= q:
                l, r = intervals.pop()
                # 右边界满足条件
                if r >= q:
                    heapq.heappush(pq,(r-l+1,r))
            # 去掉pq中不满足右边界
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            res[q] = pq[0][0] if pq else -1
        return [res[q] for q in queries]

        # # 并查集解法
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
        #     # 并查集查找下一个位置
        #     v = find(l)
        #     while v < r:
        #         ans[v] = b - a + 1
        #         par[v] = v + 1
        #         v = find(v)
        #
        # d = {val:i for i,val in enumerate(q)}
        # return [ans[d[i]] for i in queries]
