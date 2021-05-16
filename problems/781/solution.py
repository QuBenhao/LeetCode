import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numRabbits(list(test_input))

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        import math
        c = Counter(answers)
        ans = 0
        for k in c:
            ans += (math.ceil(c[k]/(k+1))) * (k+1)
        return int(ans)
