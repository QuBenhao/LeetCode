from collections import defaultdict
from heapq import heappush_max, heappop_max

import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = AuctionSystem()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class AuctionSystem:
    def __init__(self):
        self.amount = {}  # (userId, itemId) -> bidAmount
        self.item_h = defaultdict(list)  # itemId -> [(bidAmount, userId)]

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.amount[(userId, itemId)] = bidAmount
        heappush_max(self.item_h[itemId], (bidAmount, userId)) # 最大堆

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        self.amount.pop((userId, itemId), None)
        # 堆中元素在 getHighestBidder 中删除（懒删除）

    def getHighestBidder(self, itemId: int) -> int:
        h = self.item_h.get(itemId, None)
        while h:
            bidAmount, userId = h[0]
            if bidAmount == self.amount.get((userId, itemId), None):
                return userId
            # 货不对板，堆顶出价与实际不符
            heappop_max(h)
        return -1


