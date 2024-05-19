import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canSeePersonsCount(list(test_input))

    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
                ans[i] += 1
            if len(stack):
                ans[i] += 1
            stack.append(heights[i])
        return ans
