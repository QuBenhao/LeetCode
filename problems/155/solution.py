import solution
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MinStack()
        return [None] + [call_method(obj, op, *its) for op, its in zip(ops[1:], inputs[1:])]


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.stack:
            self.stack.append((val, min(val, self.getMin())))
        else:
            self.stack.append((val, val))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
