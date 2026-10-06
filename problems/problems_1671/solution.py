import solution
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumMountainRemovals(list(test_input))

    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # Longest increasing subsequences from left to right
        forward = self.LIS(nums)
        # Longest increasing subsequences from right to left
        backward = self.LIS(nums[::-1])[::-1]
        res = 0
        for i in range(n):
            # The peak cannot be at either end; both sides need at least one additional smaller element
            if forward[i] > 1 and backward[i] > 1:
                # Add both lengths for the longest mountain, subtracting 1 for the duplicated peak
                res = max(res, forward[i] + backward[i] - 1)
        return n - res

    def LIS(self, nums):
        n = len(nums)
        dp = [1] * n
        curr = [nums[0]]
        for i in range(1, n):
            # Find the position of nums[i] in curr
            idx = bisect.bisect_left(curr, nums[i])
            # If idx is at the end, extend the longest increasing subsequence
            if idx == len(curr):
                curr.append(nums[i])
            # Otherwise, replace curr[idx]
            else:
                curr[idx] = nums[i]
            # The longest increasing subsequence ending at nums[i] has length idx+1
            dp[i] = idx + 1
        return dp
