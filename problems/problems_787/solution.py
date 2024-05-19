import solution
from collections import defaultdict
from functools import lru_cache
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findCheapestPrice(*test_input)

    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        connect = defaultdict(dict)
        for a, b, c in flights:
            connect[a][b] = c

        @lru_cache(None)
        def dfs(city, remain):
            if city == dst:
                return 0
            if not remain:
                return inf
            remain -= 1
            ans = inf
            for nxt in connect[city]:
                ans = min(ans, dfs(nxt, remain) + connect[city][nxt])
            return ans

        res = dfs(src, k + 1)
        return res if res != inf else -1
