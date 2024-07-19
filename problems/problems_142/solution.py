import solution
from typing import *
from python.object_libs import list_to_linked_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        head0 = list_to_linked_list(nums0)
        res = self.detectCycle(head0)
        return res.val if res else None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        (m * 2 - a) % c = (m - a) % c
        m * 2 - a = n * c + m - a
        m = n * c
        (m + a) % c = 0
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
