import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isValid(str(test_input))

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ["(","[","{"]
        right = [")","]","}"]
        stack = []
        for c in s:
            if c in right:
                if not stack or stack[-1] != left[right.index(c)]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
