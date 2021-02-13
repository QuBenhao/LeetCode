import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestPathBinaryMatrix([x[:] for x in test_input])

    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import heapq
        m = len(grid)
        n = len(grid[0])

        frontier = []
        explored = set()

        def heuristic(position):
            return max(abs(m - 1 - position[0]), abs(n - 1 - position[1]))

        if not grid[0][0]:
            frontier.append((0, (0, 0), 1))
        while frontier:
            h, pos, cost = heapq.heappop(frontier)
            if pos == (m - 1, n - 1):
                return cost
            if pos in explored:
                continue
            explored.add(pos)
            cost += 1
            for succ in [(x, y) for x in range(pos[0] - 1, pos[0] + 2) for y in range(pos[1] - 1, pos[1] + 2)
                         if 0 <= x < m and 0 <= y < n and not grid[x][y] and (x, y) not in explored]:
                heapq.heappush(frontier, (heuristic(succ) + cost, succ, cost))
        return -1
