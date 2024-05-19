import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMin(list(test_input))

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                if right and nums[right - 1] > nums[right]:
                    left = right
                else:
                    right -= 1
        return nums[left]
