import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.singleNumber(test_input.copy())

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        slow = fast = 0
        while fast < n:
            fast += 2
            if fast >= n:
                return nums[slow]
            if nums[fast] == nums[slow]:
                slow = fast = fast + 1
            else:
                if nums[slow] == nums[slow+1]:
                    return nums[fast]
                return nums[slow]
