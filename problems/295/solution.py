import solution
import heapq
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MedianFinder()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.minHeap or num >= self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        elif len(self.minHeap) - len(self.maxHeap) < -1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap) == len(self.maxHeap):
            return float(self.minHeap[0] - self.maxHeap[0])/2
        return self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
