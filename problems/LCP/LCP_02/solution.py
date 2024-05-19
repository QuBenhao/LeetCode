import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.fraction(list(test_input))

    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """
        cont = cont[::-1]
        m, n = cont[0], 1
        for i in range(1, len(cont)):
            m, n = n + m * cont[i], m
        return [m, n]
