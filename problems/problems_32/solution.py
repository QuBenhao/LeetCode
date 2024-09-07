import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestValidParentheses(test_input)

    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    ans = max(ans, i - (stack[-1] if stack else -1))
                else:
                    stack.append(i)
        return ans
