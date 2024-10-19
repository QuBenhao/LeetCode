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
        def reverse_linked_list(head):
            pre = None
            while head:
                temp = head.next
                head.next = pre
                pre = head
                head = temp
            return pre

        l1, l2 = reverse_linked_list(l1), reverse_linked_list(l2)
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return reverse_linked_list(dummy.next)
