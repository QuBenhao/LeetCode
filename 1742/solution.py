import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        lowLimit, highLimit = test_input
        return self.countBalls(lowLimit, highLimit)

    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """

        import collections
        ans = 0
        d = collections.defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            s = 0
            while i > 0:
                s += i % 10
                i //= 10
            d[s] += 1
            ans = max(ans, d[s])
        return ans

        # import collections
        #
        # freq = collections.defaultdict(int)
        # for x in range(lowLimit, highLimit + 1):
        #     freq[sum(int(xx) for xx in str(x))] += 1
        # return max(freq.values())
