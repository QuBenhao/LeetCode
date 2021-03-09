import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeDuplicates(str(test_input))

    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for c in S:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
