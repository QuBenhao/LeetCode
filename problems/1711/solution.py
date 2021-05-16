import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPairs(list(test_input))

    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        import collections
        mod = 10 ** 9 + 7
        ans = 0
        freq = collections.defaultdict(int)
        for x in deliciousness:
            # the max sum is 2^20 + 2^20 = 2^21
            for k in range(22):
                ans += freq[2 ** k - x]
            freq[x] += 1
        return ans % mod
