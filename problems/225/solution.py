import solution
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, nums = test_input
        # Your MyQueue object will be instantiated and called as such:
        obj = MyStack()
        ans = [None]
        for i in range(1, len(ops)):
            if ops[i] == "push":
                obj.push(nums[i][0])
                ans.append(None)
            elif ops[i] == "pop":
                ans.append(obj.pop())
            elif ops[i] == "top":
                ans.append(obj.top())
            else:
                ans.append(obj.empty())
        return ans


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        n = len(self.data)
        for i in range(n - 1):
            self.data.append(self.data.popleft())
        return self.data.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        n = len(self.data)
        for i in range(n - 1):
            self.data.append(self.data.popleft())
        val = self.data.popleft()
        self.data.append(val)
        return val

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.data


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
