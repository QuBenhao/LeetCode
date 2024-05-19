import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxArea(list(test_input))

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, ans = 0, len(height) - 1, 0
        while left < right:
            if height[left] >= height[right]:
                ans = max(ans, height[right] * (right - left))
                right -= 1
            else:
                ans = max(ans, height[left] * (right - left))
                left += 1
        return ans
