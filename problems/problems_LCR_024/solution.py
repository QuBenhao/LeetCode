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

    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next
