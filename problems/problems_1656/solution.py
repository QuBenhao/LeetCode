import solution
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = OrderedStream(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.data = [None] * n
        self.ptr = 0

    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        id -= 1
        self.data[id] = value
        if id > self.ptr:
            return []
        while self.ptr < len(self.data) and self.data[self.ptr]:
            self.ptr += 1
        return self.data[id:self.ptr]
