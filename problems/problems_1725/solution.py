import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countGoodRectangles([x[:] for x in test_input])

    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        count = 0
        m = 0
        for l,w in rectangles:
            curr = min(l,w)
            if curr > m:
                count = 1
                m = curr
            elif curr == m:
                count += 1
        return count
