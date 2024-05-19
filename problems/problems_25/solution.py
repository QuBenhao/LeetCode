import solution
from typing import *
from python.object_libs import list_to_linked_list, linked_list_to_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        head = list_to_linked_list(nums)
        root = self.reverseKGroup(head, k)
        return linked_list_to_list(root)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        node = head
        for _ in range(k - 1):
            if not node:
                break
            node = node.next
        if not node:
            return head
        node.next = self.reverseKGroup(node.next, k)
        last = tail = node.next
        while head != last:
            nxt = head.next
            head.next = tail
            tail = head
            head = nxt
        return node
