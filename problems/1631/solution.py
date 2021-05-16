import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumEffortPath([x[:] for x in test_input])

    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        import heapq
        rows, cols = len(heights), len(heights[0])
        dist = [[float("inf")] * cols for _ in range(rows)]
        dirct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # a heap order by max difference
        # current path maximum difference and position x, position y
        min_heap = [(0, 0, 0)]

        while min_heap:
            diff, x, y = heapq.heappop(min_heap)
            if diff > dist[x][y]:
                continue
            if x == rows - 1 and y == cols - 1:
                return diff
            for x_, y_ in dirct:
                nx, ny = x + x_, y + y_
                if 0 <= nx < rows and 0 <= ny < cols:
                    n_diff = max(diff, abs(heights[nx][ny] - heights[x][y]))
                    if dist[nx][ny] > n_diff:
                        dist[nx][ny] = n_diff
                        heapq.heappush(min_heap, (n_diff, nx, ny))

        # # BFS + Binary search
        # from collections import deque
        #
        # def is_possible(weight):
        #     frontier = deque([(0, 0)])
        #     explored = {(0,0)}
        #     while frontier:
        #         x, y = frontier.popleft()
        #         if x == rows - 1 and y == cols - 1:
        #             return True
        #         for x_, y_ in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
        #             if (x_, y_) not in explored and 0 <= x_ < rows and 0 <= y_ < cols \
        #                     and abs(heights[x_][y_] - heights[x][y]) <= weight:
        #                 explored.add((x_,y_))
        #                 frontier.append((x_, y_))
        #     return False
        #
        # rows, cols, left, right = len(heights), len(heights[0]), 0, 10 ** 6
        #
        # while left < right:
        #     mid = (left + right) // 2
        #     if is_possible(weight=mid):
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left
