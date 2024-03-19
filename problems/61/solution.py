import solution
from object_libs import list_to_linked_list, linked_list_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        head = list_to_linked_list(nums)
        root = self.rotateRight(head, k)
        return linked_list_to_list(root)

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        right = head
        temp = k
        while right.next and k:
            right = right.next
            k -= 1
        if k:
            k -= 1
            k %= temp - k
            return self.rotateRight(head, k)

        left = head
        while right.next:
            left = left.next
            right = right.next

        right.next = head
        head = left.next
        left.next = None

        return head


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
