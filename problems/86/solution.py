import solution
from typing import *
from object_libs import list_to_linked_list, linked_list_to_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, x = test_input
        head = self.partition(list_to_linked_list(nums), x)
        return linked_list_to_list(head)

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_small, head_large = None, None
        node1, node2 = None, None
        while head:
            if head.val >= x:
                if not head_large:
                    head_large = head
                else:
                    node2.next = head
                node2 = head
            else:
                if not head_small:
                    head_small = head
                else:
                    node1.next = head
                node1 = head
            head = head.next
        if node1:
            node1.next = head_large
        if node2:
            node2.next = None
        return head_small if head_small else head_large
