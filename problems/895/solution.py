import solution
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = FreqStack()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class FreqStack(object):

    def __init__(self):
        from collections import Counter
        self.freq = []
        self.frequency = Counter()
        self.len = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        import heapq
        self.frequency[x] += 1
        heapq.heappush(self.freq, (-self.frequency[x],-self.len,x))
        self.len += 1

    def pop(self):
        """
        :rtype: int
        """
        import heapq
        val = heapq.heappop(self.freq)[2]
        self.frequency[val] -= 1
        return val
