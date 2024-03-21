import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numMusicPlaylists(*test_input)

    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        import math
        """
        F(N,L,K) = F(N - 1, L - 1, K) * N + F(N, L - 1, K) * (N - K)

        F(N - 1, L - 1, K)
        If only N - 1 in the L - 1 first songs.
        We need to put the rest one at the end of music list.
        Any song can be this last song, so there are N possible combinations.
        
        F(N, L - 1, K)
        If already N in the L - 1 first songs.
        We can put any song at the end of music list,
        but it should be different from K last song.
        We have N - K choices.
        """
        dp = [[0 for i in range(L + 1)] for j in range(N + 1)]
        for i in range(K + 1, N + 1):
            for j in range(i, L + 1):
                # i==k+1 means, say k=2, then at least we need to have 3 songs in order to populate the list,
                # and in that case, no matter how long the list is say 100000,
                # we only play those 3 songs repetitively with the same pattern therefore it is still 3!
                if i == j or i == K + 1:
                    dp[i][j] = math.factorial(i)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * i + dp[i][j - 1] * (i - K)
        return dp[N][L] % (10**9 + 7)