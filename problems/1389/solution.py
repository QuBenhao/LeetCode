import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.createTargetArray(*test_input)

    def createTargetArray(self, nums, index):
        # result_list = []
        for i in range(len(nums)):
            if index[i] != i:
                value = nums.pop(i)
                nums.insert(index[i],value)
            # result_list.insert(index[i],nums[i])
        # return result_list
        return nums
