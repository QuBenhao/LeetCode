import solution
from sortedcontainers import SortedList
import collections
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MKAverage(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


# class MKAverage:
#
#     def __init__(self, m: int, k: int):
#         self.m, self.k = m, k
#         self.deque = collections.deque()
#         self.sl = SortedList()
#         self.total = self.first_k = self.last_k = 0
#
#     def addElement(self, num: int) -> None:
#         self.total += num
#         self.deque.append(num)
#         index = self.sl.bisect_left(num)
#         if index < self.k:
#             self.first_k += num
#             if len(self.sl) >= self.k:
#                 self.first_k -= self.sl[self.k - 1]
#         if index >= len(self.sl) + 1 - self.k:
#             self.last_k += num
#             if len(self.sl) >= self.k:
#                 self.last_k -= self.sl[-self.k]
#         self.sl.add(num)
#         if len(self.deque) > self.m:
#             num = self.deque.popleft()
#             self.total -= num
#             index = self.sl.index(num)
#             if index < self.k:
#                 self.first_k -= num
#                 self.first_k += self.sl[self.k]
#             elif index >= len(self.sl) - self.k:
#                 self.last_k -= num
#                 self.last_k += self.sl[-self.k - 1]
#             self.sl.remove(num)
#
#     def calculateMKAverage(self) -> int:
#         if len(self.sl) < self.m:
#             return -1
#         return (self.total - self.first_k - self.last_k) // (self.m - 2 * self.k)


class MKAverage(object):

    def __init__(self, m, k):
        """
        :type m: int
        :type k: int
        """
        self.m, self.k, self.sum = m, k, 0
        self.lower, self.middle, self.upper = SortedList(), SortedList(), SortedList()
        self.nums = collections.deque()

    def shiftLeft(self, l_list, r_list):
        l_list.add(r_list.pop(0))

    def shiftRight(self, l_list, r_list):
        r_list.add(l_list.pop())

    def addElement(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.nums.append(num)
        if self.lower and self.lower[-1] >= num:
            self.lower.add(num)
        elif self.upper and self.upper[0] <= num:
            self.upper.add(num)
        else:
            self.middle.add(num)
            self.sum += num

        while len(self.lower) > self.k:
            self.sum += self.lower[-1]
            self.shiftRight(self.lower, self.middle)
        while len(self.upper) > self.k:
            self.sum += self.upper[0]
            self.shiftLeft(self.middle, self.upper)

        if len(self.nums) > self.m:
            d = self.nums.popleft()
            if self.lower.bisect_left(d) < self.k:
                self.lower.remove(d)
            elif self.middle.bisect_left(d) < len(self.middle):
                self.middle.remove(d)
                self.sum -= d
            else:
                self.upper.remove(d)

        if len(self.nums) >= self.m:
            while len(self.lower) < self.k:
                self.sum -= self.middle[0]
                self.shiftLeft(self.lower, self.middle)
            while len(self.upper) < self.k:
                self.sum -= self.middle[-1]
                self.shiftRight(self.middle, self.upper)

    def calculateMKAverage(self):
        """
        :rtype: int
        """
        if len(self.nums) < self.m:
            return -1
        return self.sum // (self.m - self.k * 2)

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
