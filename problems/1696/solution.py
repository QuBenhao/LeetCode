import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxResult(*test_input)

    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = list(nums)
        window = [[0, nums[0]]]
        for i in range(1, n):
            # jump from starting of the window to current value
            dp[i] += window[0][1]

            # if the latest near element is smaller than current dp,
            # which means we should always jump to current index
            while window and window[-1][1] < dp[i]:
                window.pop()

            window.append([i, dp[i]])

            # make sure the window between the first index and current index is not exceeding jump k
            if i - window[0][0] == k:
                window.pop(0)

        return dp[-1]
