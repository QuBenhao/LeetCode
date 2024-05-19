import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kthFactor(*test_input)

    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        for i in range(1,n+1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        return -1
