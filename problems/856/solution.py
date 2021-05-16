import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.scoreOfParentheses(str(test_input))

    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for s in S:
            if s == ')':
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    score = 0
                    while stack and stack[-1] != '(':
                        score += stack.pop()
                    stack.pop()
                    stack.append(2 * score)
            else:
                stack.append(s)
        return sum(stack)
