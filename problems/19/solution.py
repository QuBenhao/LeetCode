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
        nums0, n = test_input
        head0 = list_to_linked_list(nums0)
        res = self.removeNthFromEnd(head0, n)
        return linked_list_to_list(res)

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = dummy_head = ListNode(next=head)
        fast = head
        while fast and n:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_head.next
