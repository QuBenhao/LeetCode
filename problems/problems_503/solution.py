import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nextGreaterElements(test_input.copy())

    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)
        # ans = [-1] * n
        # stack = []
        # for i in range(n):
        #     while stack and nums[stack[-1]] < nums[i]:
        #         ans[stack.pop()] = nums[i]
        #     stack.append(i)
        # for i in range(n):
        #     while stack and nums[stack[-1]] < nums[i]:
        #         ans[stack.pop()] = nums[i]
        # return ans

        n = len(nums)
        stack, ans = [], [-1] * n
        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i%n]:
                ans[stack.pop()] = nums[i%n]
            if i < n:
                stack.append(i)
            elif not stack:
                break
        return ans
