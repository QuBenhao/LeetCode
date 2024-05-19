import solution
from heapq import heappop, heappush
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        # Your SeatManager object will be instantiated and called as such:
        obj = SeatManager(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class SeatManager(object):

    def __init__(self, n: int):
        self.avl = [i for i in range(1,n+1)]

    def reserve(self) -> int:
        return heappop(self.avl)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.avl, seatNumber)
