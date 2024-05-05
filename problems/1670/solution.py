import solution
from collections import deque
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input

        # Your FrontMiddleBackQueue object will be instantiated and called as such:
        obj = FrontMiddleBackQueue()
        # obj.pushFront(val)
        # obj.pushMiddle(val)
        # obj.pushBack(val)
        # param_4 = obj.popFront()
        # param_5 = obj.popMiddle()
        # param_6 = obj.popBack()

        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class FrontMiddleBackQueue(object):
    def __init__(self):
        self.front = deque([])
        self.back = deque([])

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        self.front.append(val)
        self.balance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.front:
            val = self.front.popleft()
        else:
            val = self.back.popleft()
        self.balance()
        return val

    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) >= len(self.back):
            val = self.front.pop()
        else:
            val = self.back.popleft()
        self.balance()
        return val

    def popBack(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.back:
            val = self.back.pop()
        else:
            val = self.front.pop()
        self.balance()
        return val

    def balance(self):
        while len(self.back) > len(self.front) + 1:
            self.front.append(self.back.popleft())
        while len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
