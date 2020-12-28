import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, m = test_input
        return self.tilingRectangle(n, m)

    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # backtracking

        # self.best = m * n
        #
        # def dfs(height, moves):
        #     if all(h == n for h in height):
        #         self.best = min(self.best, moves)
        #         return
        #     if moves >= self.best:
        #         return
        #     min_height = min(height)
        #     idx = height.index(min_height)
        #     ridx = idx + 1
        #     while ridx < m and height[ridx] == min_height:
        #         ridx += 1
        #     for i in range(min(ridx - idx, n - min_height), 0, -1):
        #         new_height = height[:]
        #         for j in range(i):
        #             new_height[idx + j] += i
        #         dfs(new_height, moves + 1)
        #
        # dfs([0] * m, 0)
        # return self.best

        import heapq
        # Credits to StrongerXi
        # Use the least number of squares to fill up the remaining area as a lower bound.
        total_area = m * n
        dp = [0] * (total_area + 1)
        for i in range(1, total_area + 1):
            dp[i] = 1 + min(dp[i - k ** 2] for k in range(1, int(i ** 0.5) + 1))

        height = [0] * m
        q = []
        for i in range(min(m, n), 0, -1):
            # Push to heap: (heuristic, moves, size, height)
            heapq.heappush(q, (1 + dp[total_area - i ** 2], 1, i, height))

        while q:
            guess, moves, size, height = heapq.heappop(q)
            idx = height.index(min(height))
            height = height[:]
            for i in range(size):
                height[idx + i] += size
            if all(h == n for h in height):
                return moves
            min_height = min(height)
            idx = height.index(min_height)
            ridx = idx + 1
            while ridx < m and height[ridx] == min_height:
                ridx += 1
            for i in range(min(ridx - idx, n - min_height), 0, -1):
                guess = dp[total_area - sum(height) - i ** 2]
                heapq.heappush(q, (moves + 1 + guess, moves + 1, i, height))
