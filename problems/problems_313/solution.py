import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nthSuperUglyNumber(*test_input)

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        m = len(primes)
        # dp[i] is the (i+1)th ugly number
        dp = [1] * n
        # Ugly number, index of the ugly number just multiplied, prime factor
        pq = [(p, 0, i) for i, p in enumerate(primes)]

        for i in range(1, n):
            # Current smallest new ugly number
            dp[i] = pq[0][0]
            # Pop every entry equal to this value, then reinsert using the next ugly number to multiply
            while pq and pq[0][0] == dp[i]:
                _, idx, p = heapq.heappop(pq)
                heapq.heappush(pq, (dp[idx + 1] * primes[p], idx + 1, p))
        return dp[-1]
