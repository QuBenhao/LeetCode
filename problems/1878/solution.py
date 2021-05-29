import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getBiggestThree([x[:] for x in test_input])

    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        pq = []
        maxlen = min(m, n)
        if maxlen % 2 == 0:
            maxlen -= 1
        direct = [(1,1),(-1,1),(-1,-1),(1,-1)]
        for i in range(maxlen, 0, -2):
            if i == 1:
                for k in range(m):
                    for j in range(n):
                        heapq.heappush(pq, -grid[k][j])
            else:
                l = i//2
                # 横的长，纵的长
                for h in range(l, n-l):
                    for s in range(m-i+1):
                        sum_ = 0
                        x,y = h,s
                        count = d = 0
                        # 顶点为h,s
                        while d < 4:
                            if count == l:
                                count = 0
                                d += 1
                                continue
                            sum_ += grid[y][x]
                            x += direct[d][0]
                            y += direct[d][1]
                            count += 1
                        heapq.heappush(pq, -sum_)
        ans = []
        explored = set()
        while len(ans) < 3 and pq:
            val = - heapq.heappop(pq)
            if val in explored:
                continue
            explored.add(val)
            ans.append(val)
        return ans
