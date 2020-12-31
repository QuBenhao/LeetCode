import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestRectangleArea(list(test_input))

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        # start with -1 and heights[-1] = 0
        stack = [-1]
        heights.append(0)
        ans = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                # heights[j] > heights[stack[-1]) and heights[j] > heights[i]
                ans = max(ans, heights[j] * (i - stack[-1] - 1))
            stack.append(i)

        return ans
