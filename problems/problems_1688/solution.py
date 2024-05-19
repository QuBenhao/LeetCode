import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfMatches(test_input)

    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        count = 0
        while n >= 2:
            if n % 2 == 0:
                count += n/2
                n /= 2
            else:
                count += (n-1)/2
                n = (n+1)/2
        return count
