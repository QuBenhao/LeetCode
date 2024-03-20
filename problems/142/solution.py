import solution
from object_libs import list_to_linked_list_cycle


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, pos = test_input
        head = list_to_linked_list_cycle(nums, pos)
        return node.val if (node := self.detectCycle(head)) else None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return None

            # slow == ENTRY, fast == HEAD -> ENTRY * 2
            # slow == fast:
            # t % C == 2 * t + HEAD -> ENTRY % C
            # t % C == - HEAD -> ENTRY
            if fast == slow:
                break

        if not fast:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
