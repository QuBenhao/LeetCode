import solution
from typing import *
from python.object_libs import list_to_linked_list, linked_list_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, nums1 = test_input
        head0 = list_to_linked_list(nums0)
        head1 = list_to_linked_list(nums1)
        res = self.addTwoNumbers(head0, head1)
        return linked_list_to_list(res)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(node: Optional[ListNode]):
            if not node or not node.next:
                return node
            new_head = reverse_list(node.next)
            node.next.next = node
            node.next = None
            return new_head

        l1r, l2r = reverse_list(l1), reverse_list(l2)
        dummy, cur = ListNode(), 0
        nd = dummy
        while l1r or l2r or cur:
            if l1r:
                cur += l1r.val
                l1r = l1r.next
            if l2r:
                cur += l2r.val
                l2r = l2r.next
            nd.next = ListNode(cur % 10)
            nd = nd.next
            cur //= 10
        return reverse_list(dummy.next)
