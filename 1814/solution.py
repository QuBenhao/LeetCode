import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countNicePairs(list(test_input))

    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        mod = 10 ** 9 + 7
        d = Counter()
        for n in nums:
            d[n - int(str(n)[::-1])] += 1
        ans = 0
        for k in d:
            ans += d[k] * (d[k] - 1) // 2
        return ans % mod
