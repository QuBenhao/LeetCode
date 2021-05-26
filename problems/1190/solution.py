import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reverseParentheses(str(test_input))

    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                temp = reversed(stack.pop())
                stack[-1] += temp
            else:
                stack[-1].append(c)
        return "".join(stack[0])
