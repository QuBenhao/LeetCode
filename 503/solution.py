import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nextGreaterElements(test_input.copy())

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack, res = [], [-1] * n
        for i in range(n*2):
            temp = i
            if i >= n:
                i -= n
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            if temp < n:
                stack.append(i)
            elif not stack:
                break
        return res
