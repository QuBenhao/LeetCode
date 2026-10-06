import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxFrequency(*test_input)

    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = j = 0
        # Sort ascending to check whether k can raise all values from i through j to nums[j]
        nums.sort()
        for j in range(len(nums)):
            # Add nums[j] to the available step budget k
            k += nums[j]
            # nums[j] * (j - i + 1) is the number of steps to raise an all-zero window to nums[j]
            # If k is insufficient, remove the leftmost value, which is farthest below nums[j]
            # If i and j fail the inequality, move the left pointer once to preserve the previous window length
            # (Later windows may remain invalid after the longest one; we only seek a longer valid window)
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1
