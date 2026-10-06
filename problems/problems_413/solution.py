import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfArithmeticSlices(list(test_input))

    def numberOfArithmeticSlices(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        # n = len(nums)
        # # Previous difference
        # last = None
        # # Length of the preceding run of equal differences
        # last_len = ans = 0
        # for i in range(1, n):
        #     # Equal difference: extend the run by one
        #     if nums[i] - nums[i-1] == last:
        #         last_len += 1
        #     # Otherwise, the run contains only the difference between these two values
        #     else:
        #         last_len = 1
        #     # This contributes len-1 possibilities ending here
        #     ans += last_len - 1
        #     last = nums[i] - nums[i-1]
        # return ans

        n = len(nums)
        l = r = ans = 0
        # At l = n-2, too few values remain to form another arithmetic sequence
        while l < n - 2:
            d = nums[l + 1] - nums[l]
            while r < n - 1 and nums[r + 1] - nums[r] == d:
                r += 1
            # k = r - l + 1, (k-1)*(k-2)/2 = (r-l) * (r-l-1)/2
            ans += (r-l) *(r-l-1)//2
            l = r
        return ans
