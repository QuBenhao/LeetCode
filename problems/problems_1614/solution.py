import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDepth(test_input)

    def maxDepth(self, s: str) -> int:
        max_c = count = 0
        for c in s:
            if c == '(':
                count += 1
                max_c = max(count,max_c)
            if c == ')':
                count -= 1
        return max_c
