import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeDuplicates(test_input.copy())

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = count = -1
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                count = 1
            else:
                count += 1
            if count > 2:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums),nums

    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     backward = 0
    #     forward = 2
    #     while forward < len(nums):
    #         if nums[forward] != nums[backward] and nums[backward + 1] == nums[backward]:
    #             backward = forward
    #             forward += 2
    #         elif nums[forward] == nums[backward]:
    #             nums[forward:] = nums[forward + 1:]
    #         else:
    #             forward += 1
    #             backward += 1
    #     return len(nums)
