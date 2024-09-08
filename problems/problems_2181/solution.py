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
        res = self.mergeNodes(head0)
        return linked_list_to_list(res)

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node, cur = dummy, head.next
        while cur:
            s = 0
            while cur and cur.val != 0:
                s += cur.val
                cur = cur.next
            node.next = ListNode(s)
            node = node.next
            if cur:
                cur = cur.next
        return dummy.next
