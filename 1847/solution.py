import solution
from sortedcontainers import SortedList
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        rooms, queries = test_input
        return self.closestRoom([x[:] for x in rooms], [x[:] for x in queries])

    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rooms.sort(key=lambda x:(x[1],x[0]))
        ans = [-1] * len(queries)
        index_dict = defaultdict(list)
        for i,v in enumerate(queries):
            index_dict[tuple(v)].append(i)
        sl = SortedList()
        for idx,size in sorted(queries, key=lambda x:(-x[1],x[0])):
            while rooms and rooms[-1][1] >= size:
                i,s = rooms.pop()
                sl.add(i)
            if sl:
                p = sl.bisect_left(idx)
                cand = []
                if p > 0:
                    cand.append(sl[p-1])
                if p < len(sl):
                    cand.append(sl[p])
                res = min(cand, key=lambda x:abs(x-idx))
                for i in index_dict[idx,size]:
                    ans[i] = res
        return ans
