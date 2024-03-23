import solution
from object_libs import list_to_linked_list, linked_list_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums1, a, b, nums2 = test_input
        head1, head2 = list_to_linked_list(nums1), list_to_linked_list(nums2)
        root = self.mergeInBetween(head1, a, b, head2)
        return linked_list_to_list(root)

    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        if a == list1.val:
            root = list2
        else:
            root = list1
        l1 = list1
        node = list2
        count = 1
        while count < a:
            l1 = l1.next
            count += 1
        r1 = l1
        while count <= b:
            r1 = r1.next
            count += 1
        r1 = r1.next
        while node.next is not None:
            node = node.next
        l1.next = list2
        node.next = r1
        return root


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
