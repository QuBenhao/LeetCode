import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDifference(*test_input)

    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        m = max(nums)
        # Difference array
        diff = [[0] * (m + 1)]
        for num in nums:
            diff.append(list(diff[-1]))
            diff[-1][num] += 1

        ans = []
        for l, r in queries:
            res = m  # The answer cannot exceed the maximum value
            last = -m  # Ensure the first difference does not affect the result
            # Use prefix differences to find which values occur from l through r
            for i in range(1, m + 1):
                if diff[r + 1][i] - diff[l][i] > 0:
                    res = min(res, i - last)
                    last = i
            ans.append(res if res < m else -1)
        return ans
