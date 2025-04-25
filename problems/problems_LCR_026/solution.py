import solution
from typing import *
from python.object_libs import list_to_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        head0 = list_to_linked_list(nums0)
        self.reorderList(head0)
        return linked_list_to_list(head0)

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        mid = (n + 1) // 2
        mid_node = head
        for _ in range(mid - 1):
            mid_node = mid_node.next
        
        reservsed_head = mid_node.next
        mid_node.next = None
        cur = reservsed_head
        while cur and cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = reservsed_head
            reservsed_head = nxt

        cur = head
        while reservsed_head:
            next = cur.next
            cur.next = reservsed_head
            rn = reservsed_head.next
            reservsed_head.next = next
            reservsed_head = rn
            cur = next
