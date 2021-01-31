import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nextPermutation(list(test_input))

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        index = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if index > -1:
            for i in range(n-1,index,-1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break

        left, right = index + 1, n - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
