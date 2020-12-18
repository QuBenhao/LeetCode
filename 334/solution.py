import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.increasingTriplet(test_input.copy())

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n = len(nums)
        # if n < 3:
        #     return False
        # left_min = nums[0]
        # right_max = max(nums[2:])
        # for j in range(1, n - 1):
        #     if nums[j-1] < left_min:
        #         left_min = nums[j-1]
        #     if nums[j+1] == right_max:
        #         right_max = max(nums[j+1:])
        #     if left_min < nums[j] < right_max:
        #         return True
        #
        # return False

        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
