import solution


class Solution(solution.Solution):
    def solve(self, test_input):
        return self.soupServings(test_input)

    def soupServings(self, N: int) -> float:
        """
        :type N: int
        :rtype: float
        """
        N = (N + 24) // 25  # Convert N to the number of 25 ml servings
        if N >= 178:
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
            self.memo[(a,b)] = 0.25 * (f(a-4,b) + f(a-3,b-1) + f(a-2,b-2) + f(a-1,b-3))
            return self.memo[(a,b)]

        self.memo = {}
        return f(N,N)
