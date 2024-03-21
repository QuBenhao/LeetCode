import solution
from object_libs import list_to_linked_list_cycle


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head = list_to_linked_list_cycle(*test_input)
        return self.hasCycle(head)

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if fast == slow:
                return True
        return False


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
