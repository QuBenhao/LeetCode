import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.search(*test_input)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            pivot = nums[mid]
            if target == nums[mid] or target == nums[left] or target == nums[right]:
                return True
            # right
            if pivot < nums[left]:
                # point between left and mid
                # left goes mid + 1 only if nums[mid] < target < nums[left]
                if nums[mid] < target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # left
            elif pivot > nums[left]:
                # point between mid and right (maybe?)
                # right goes left only if nums[left] < target < nums[mid]
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # don't know where the point is, but at least left is not what we want
            else:
                left += 1
        return False
