import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumUniqueSubarray(test_input.copy())

    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        vals = []
        res = 0
        last = 0
        for i in range(n):
            if nums[i] in vals:
                temp = vals.index(nums[i])
                for j in range(temp):
                    last -= vals.pop(0)
                vals.pop(0)
                res = max(res,last)
            else:
                last += nums[i]
                res = max(res,last)
            vals.append(nums[i])
        return res
