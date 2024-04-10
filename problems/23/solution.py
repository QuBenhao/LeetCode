import solution
from typing import *
from object_libs import list_to_linked_list, linked_list_to_list
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums_arr = test_input
        heads = [list_to_linked_list(nums) for nums in nums_arr]
        res = self.mergeKLists(heads)
        return linked_list_to_list(res)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy, pq = ListNode(0), []
        node = dummy
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i))
        while pq:
            v, idx = heapq.heappop(pq)
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(pq, (lists[idx].val, idx))
            node.next = ListNode(v)
            node = node.next
        return dummy.next
