import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target = test_input
        return self.twoSum(nums, target)

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        for i in range(len(nums)):
            try:
                j = list.index(nums, target - nums[i], i + 1)
                return [i, j]
            except:
                continue
