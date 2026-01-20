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
        self.bid_map = {} # (itemId, userId) -> bidAmount
        self.item_map = defaultdict(list) # itemId -> (bidAmount, userId)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.bid_map[(itemId, userId)] = bidAmount
        heappush_max(self.item_map[itemId], (bidAmount, userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        self.bid_map.pop((itemId, userId), None)

    def getHighestBidder(self, itemId: int) -> int:
        h = self.item_map[itemId]
        while h:
            bid_amount, user_id = h[0]
            if self.bid_map.get((itemId, user_id), None) == bid_amount:
                return user_id
            heappop_max(h)
        return -1
