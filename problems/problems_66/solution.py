import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.plusOne(test_input)

    def plusOne(self, digits):
        n, cur = len(digits), 1
        for i, d in enumerate(digits[::-1]):
            cur, digits[n - 1 - i] = divmod(d + cur, 10)
            if not cur:
                break
        return digits if not cur else [cur] + digits
