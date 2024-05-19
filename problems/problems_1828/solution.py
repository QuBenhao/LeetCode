import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPoints(*test_input)

    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def in_cir(x1, x2, y1, y2, r):
            return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r * r

        ans = [0] * len(queries)
        for i, v in enumerate(queries):
            x1, y1, r = v
            for x2, y2 in points:
                if in_cir(x1, x2, y1, y2, r):
                    ans[i] += 1
        return ans
