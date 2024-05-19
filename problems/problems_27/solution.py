import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeElement(*test_input)

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        for num in nums:
            if num != val:
                nums[idx] = num
                idx += 1
        return idx
