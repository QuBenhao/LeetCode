import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, nums = test_input
        # Your MyQueue object will be instantiated and called as such:
        obj = MyQueue()
        ans = [None]
        for i in range(1, len(ops)):
            if ops[i] == "push":
                obj.push(nums[i][0])
                ans.append(None)
            elif ops[i] == "pop":
                ans.append(obj.pop())
            elif ops[i] == "peek":
                ans.append(obj.peek())
            else:
                ans.append(obj.empty())
        return ans


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.push_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.push_stack and not self.pop_stack
