import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getCollisionTimes([x[:] for x in test_input])

    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        stack = []
        n = len(cars)
        res = [-1] * n
        for i in range(n-1, -1, -1):
            p, s = cars[i]
            p = float(p)
            while stack and (s <= cars[stack[-1]][1] or (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack:
                res[i] = (cars[stack[-1]][0] - p) / (s - cars[stack[-1]][1])
            stack.append(i)
        return res
