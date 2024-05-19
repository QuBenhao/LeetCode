import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxAverageRatio(*test_input)

    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        import heapq
        pq = [(- float(p+1)/(t+1) + float(p)/t, p, t) for p, t in classes]
        heapq.heapify(pq)
        while extraStudents:
            inc, p, t = heapq.heappop(pq)
            p += 1
            t += 1
            heapq.heappush(pq, (- float(p + 1)/(t+1) + float(p)/t, p, t))
            extraStudents -= 1
        return sum(float(p[1])/p[2] for p in pq) / len(classes)
