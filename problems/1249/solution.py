import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minRemoveToMakeValid(test_input)

    def minRemoveToMakeValid(self, s: str) -> str:
        stack, cur = [], ''
        for c in s:
            if c == '(':
                stack += [cur]
                cur = ''
            elif c == ')':
                if stack:
                    cur = stack.pop() + '(' + cur + ')'
            else:
                cur += c

        while stack:
            cur = stack.pop() + cur

        return cur

        # stack = []
        # remove = []
        # for i,c in enumerate(s):
        #     if c == ')':
        #         if not stack:
        #             remove.append(i)
        #         else:
        #             stack.pop()
        #     elif c == '(':
        #         stack.append(i)
        # remove = remove + stack
        # remove.append(len(s))
        # ans = ""
        # last = 0
        # for r in remove:
        #     ans += s[last:r]
        #     last = r+1
        # return ans
