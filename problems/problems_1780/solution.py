import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkPowersOfThree(test_input)

    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

        # import math
        # if n <= 0:
        #     return False
        #
        # def bfs(num):
        #     if num < 0:
        #         return False
        #     elif num == 0:
        #         return True
        #
        #     max_k = int(math.log(num, 3))
        #     for i in range(max_k, -1, -1):
        #         if i in explored:
        #             continue
        #         explored.add(i)
        #         if bfs(num - 3 ** i):
        #             return True
        #     return False
        #
        # explored = set()
        # return bfs(n)
