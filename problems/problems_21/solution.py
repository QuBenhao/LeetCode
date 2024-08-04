import solution
from python.object_libs import linked_list_to_list, list_to_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
        dummy = ListNode()
        node = dummy
        while l1 or l2:
            if l2 is None or (l1 and l1.val <= l2.val):
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        return dummy.next
