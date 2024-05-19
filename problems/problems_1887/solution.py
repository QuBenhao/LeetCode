import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reductionOperations(list(test_input))

    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        res = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                res += i
        return res
