import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumLength(str(test_input))

    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            current = s[left]
            while left < right and s[left] == current:
                left += 1
            while right >= left and s[right] == current:
                right -= 1
        return right - left + 1
