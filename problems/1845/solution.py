import solution
from heapq import heappop, heappush


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, nums = test_input
        # Your SeatManager object will be instantiated and called as such:
        obj = SeatManager(nums[0][0])
        ans = [None]
        for i in range(1, len(ops)):
            if ops[i] == "reserve":
                ans.append(obj.reserve())
            else:
                obj.unreserve(nums[i][0])
                ans.append(None)
        return ans


class SeatManager(object):

    def __init__(self, n: int):
        self.avl = [i for i in range(1,n+1)]

    def reserve(self) -> int:
        return heappop(self.avl)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.avl, seatNumber)
