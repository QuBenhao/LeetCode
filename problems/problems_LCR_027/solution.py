import solution
from typing import *
from python.object_libs import list_to_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        head0 = list_to_linked_list(nums0)
        return self.isPalindrome(head0)

    def isPalindrome(self, head: ListNode) -> bool:
        def reserve_list(node: ListNode):
            prev = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev


        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        reversed_head = reserve_list(slow)

        try:
            cur1, cur2 = head, reversed_head
            while cur2:
                if cur1.val != cur2.val:
                    return False
                cur1 = cur1.next
                cur2 = cur2.next
            return True
        finally:
            reserve_list(reversed_head)
