import solution
from typing import *
from python.object_libs import list_to_linked_list, list_to_linked_list_cycle, linked_list_to_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, pos0 = test_input
        head0 = list_to_linked_list_cycle(nums0, pos0)
        res = self.detectCycle(head0)
        return res.val if res else None

    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        # a + x + b = 2(a + x) => b = a + x
        # So, when slow and fast meet, slow has walked a + x steps, and fast has walked a + x + b steps
        # Then start from head and the meeting point, they will meet at the cycle start point
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
