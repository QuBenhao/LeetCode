import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallerNumbersThanCurrent(test_input)

    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = {}

        # LeetCode does not support list.copy()
        # c_nums = list.copy(nums)
        c_nums = []
        for i in nums:
            c_nums.append(i)

        list.sort(c_nums)
        for i in range(len(c_nums)):
            if c_nums[i] not in num_set:
                num_set[c_nums[i]] = i

        result = []
        for i in nums:
            result.append(num_set[i])
        return result
