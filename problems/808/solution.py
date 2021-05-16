import solution

class Solution(solution.Solution):
    def solve(self, test_input):
        return self.soupServings(test_input)

    def soupServings(self, N):
        """
        :type N: int
        :rtype: float
        """
        if N > 4800:
            return 1

        def f(a,b):
            if (a,b) in self.memo:
                return self.memo[(a,b)]

            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            self.memo[(a,b)] = 0.25 * (f(a-100,b) + f(a-75,b-25) + f(a-50,b-50) + f(a-25,b-75))
            return self.memo[(a,b)]

        self.memo = {}
        return f(N,N)
