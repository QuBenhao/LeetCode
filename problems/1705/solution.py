import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.eatenApples(*test_input)

    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        import heapq
        queue = []
        n = len(apples)
        i = 0
        count = 0
        while i < n or queue:
            if i < n:
                heapq.heappush(queue, [i + days[i] - 1, apples[i]])
            while queue and (queue[0][0] < i or queue[0][1] == 0):
                heapq.heappop(queue)
            if queue:
                queue[0][1] -= 1
                count += 1
            i += 1
        return count
