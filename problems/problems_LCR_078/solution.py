import heapq

import solution
from typing import *
from python.object_libs import list_to_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums_arr = test_input
        heads = [list_to_linked_list(nums) for nums in nums_arr]
        res = self.mergeKLists(heads)
        return linked_list_to_list(res)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = []
        for i, head in enumerate(lists):
            if not head:
                continue
            heapq.heappush(pq, (head.val, i, head))
        dummy = ListNode(0)
        curr = dummy
        while pq:
            val, i, node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))
        return dummy.next
