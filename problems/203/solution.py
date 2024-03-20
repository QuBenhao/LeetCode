import solution
from object_libs import list_to_linked_list, linked_list_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, val = test_input
        head = list_to_linked_list(nums)
        root = self.removeElements(head, val)
        return linked_list_to_list(root)

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        node, last = head, dummy
        while node:
            if node.val == val:
                last.next = node.next
            else:
                last = last.next
            node = node.next
        return dummy.next

        # if not head:
        #     return head
        # head.next = self.removeElements(head.next, val)
        # return head.next if head.val == val else head


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
