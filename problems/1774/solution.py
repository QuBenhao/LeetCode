import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.closestCost(*test_input)

    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        self.ans = float("inf")

        def bfs(index, curr):
            if curr >= target or index == len(toppingCosts):
                if abs(curr - target) < abs(self.ans - target):
                    self.ans = curr
                elif abs(curr - target) == abs(self.ans - target):
                    self.ans = min(self.ans, curr)
                return
            bfs(index + 1, curr)
            bfs(index + 1, curr + toppingCosts[index])
            bfs(index + 1, curr + 2 * toppingCosts[index])

        for b in baseCosts:
            bfs(0, b)
        return self.ans
