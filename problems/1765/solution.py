import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.highestPeak([x[:] for x in test_input])

    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """

        # # multiple BFS
        # from collections import deque
        # m, n = len(isWater), len(isWater[0])
        # ans = [[float("inf") for _ in range(n)] for _ in range(m)]
        # queue = deque()
        # for i in range(m):
        #     for j in range(n):
        #         if isWater[i][j]:
        #             queue.append((i,j))
        #             ans[i][j] = 0
        # while queue:
        #     r, c = queue.popleft()
        #     for x, y in [(r+1,c), (r-1,c), (r, c+1), (r, c-1)]:
        #         if 0 <= x < m and 0 <= y < n and ans[r][c] + 1 < ans[x][y]:
        #             ans[x][y] = ans[r][c] + 1
        #             queue.append((x,y))
        # return ans

        m, n = len(isWater), len(isWater[0])
        ans = [[-1 for _ in range(n)] for _ in range(m)]
        frontier = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    frontier.append((i,j))
                    ans[i][j] = 0
        level = 1
        while frontier:
            next_ = set()
            for x,y in frontier:
                for i,j in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                    if 0 <= i < m and 0 <= j < n and ans[i][j] == -1:
                        next_.add((i,j))
                        ans[i][j] = level
            frontier = next_
            level += 1
        return ans
