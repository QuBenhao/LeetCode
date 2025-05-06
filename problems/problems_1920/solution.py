import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.buildArray(list(test_input))

    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return [nums[nums[i]] for i in range(len(nums))]
        
        for i, num in enumerate(nums):
            if nums[i] < 0:
                continue
            cur = i
            while nums[cur] != i:
                nxt = nums[cur]
                nums[cur] = ~nums[nxt]
                cur = nxt
            nums[cur] = ~num
        
        for i, num in enumerate(nums):
            nums[i] = ~num
        return nums
