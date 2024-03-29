import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validateStackSequences(*test_input)

    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        index, n = 0, len(popped)
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return index == n
