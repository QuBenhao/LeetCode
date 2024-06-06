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
        res = self.reverseList(head0)
        return linked_list_to_list(res)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or head.next is None:
        #     return head
        # new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head

        dummy = ListNode()
        while head:
            tmp = dummy.next
            dummy.next = head
            head = head.next
            dummy.next.next = tmp
        return dummy.next
