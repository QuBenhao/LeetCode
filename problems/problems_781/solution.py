from collections import defaultdict

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numRabbits(list(test_input))

    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        ans = 0
        explored = defaultdict(int)
        for i in answers:
            if not explored[i] % (i + 1):
                ans += i + 1
            explored[i] += 1
        return ans
