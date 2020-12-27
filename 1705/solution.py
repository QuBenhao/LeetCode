import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        apples, days = test_input
        return self.eatenApples(list(apples),list(days))

    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
