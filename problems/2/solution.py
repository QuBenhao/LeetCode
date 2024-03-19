import solution
from object_libs import list_to_linked_list, linked_list_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        l1_nums, l2_nums = test_input

        l1 = list_to_linked_list(l1_nums)
        l2 = list_to_linked_list(l2_nums)
        root = self.addTwoNumbers(l1, l2)
        return linked_list_to_list(root)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        pointer = root = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            if carry >= 10:
                s = carry - 10
                carry = 1
            else:
                s = carry
                carry = 0
            pointer.next = ListNode(s)
            pointer = pointer.next
        return root.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
