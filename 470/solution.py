import solution
import random


class Solution(solution.Solution):
    def solve(self, test_input=None):
        times = test_input
        ans = []
        for i in range(times):
            ans.append(self.rand10())
        return ans

    def rand10(self):
        """
        :rtype: int
        """

        c = (rand7() - 1) * 7 + rand7() - 1
        if c < 40:
            return (c % 10) + 1
        else:
            c = (c - 40) * rand7() + rand7() - 1
            if c < 60:
                return (c % 10) + 1
        return self.rand10()


# The rand7() API is already defined for you.
def rand7():
    return random.randrange(1, 8, 1)
