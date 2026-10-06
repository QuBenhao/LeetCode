import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfArithmeticSlices(list(test_input))

    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # For three values to form an arithmetic subsequence, use the first two values' difference and look for the second value plus that difference later
        # For example, in [2, 4, 6, 6, 6], 2 and 4 form an answer with each of the three 6s
        # For a fixed prefix, track the required val and the number of preceding arithmetic subsequences corresponding to it

        n, ans = len(nums), 0
        dp = [Counter() for _ in range(n)]
        # Current final value of an arithmetic subsequence (possibly only this value so far)
        for i in range(n - 1):
            # Can adding this value extend an arithmetic subsequence ending there?
            for j in range(i + 1, n):
                # Current difference, used to match arithmetic subsequences ending at i
                diff = nums[j] - nums[i]
                # If a subsequence ending there has difference diff, j extends it; add one more for the new pair [i,j]
                # Otherwise, j and i form an initial pair with count (0+1); a later value differing from j by diff can complete a subsequence
                dp[j][diff] += dp[i][diff] + 1
                # Combining i, j, and the preceding subsequences ending at i with difference diff gives this many new arithmetic subsequences
                # As in yesterday's problem, [i] and [j] produce a valid subsequence only when [i] already ends one with difference diff (at least two values, making at least three with j)
                ans += dp[i][diff]
        return ans
