import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.clumsy(test_input)

    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        clumsy(n) = n * (n-1) // (n-2) + (n-3) - (n-4) * (n-5) // (n-6) + (n-7) - (n-8) * (n-9) // (n-10) + ...
                  = (n+1) + (n-3) - (n-3) + (n-7) - (n-7) + ...
                  = (n+1) + ...
        """
        return [0, 1, 2, 6, 7][N] if N < 5 else N + [1, 2, 2, -1][N % 4]

        # if N > 4:
        #     ans = N * (N-1) // (N-2) + (N-3)
        #     N -= 4
        # elif N == 4:
        #     return 7
        # elif N == 3:
        #     return 6
        # else:
        #     return N
        #
        # while N > 4:
        #     ans -= N * (N-1) // (N-2) - (N-3)
        #     N -= 4
        #
        # if N == 4:
        #     ans -= N * (N-1) // (N-2) - (N-3)
        # elif N == 3:
        #     ans -= N * (N-1) // (N-2)
        # elif N == 2:
        #     ans -= N * (N-1)
        # else:
        #     ans -= N
        # return ans
