import solution
from python.object_libs import linked_list_to_list, list_to_linked_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums1, nums2 = test_input
        head1, head2 = list_to_linked_list(nums1), list_to_linked_list(nums2)
        root = self.mergeTwoLists(head1, head2)
        return linked_list_to_list(root)

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
